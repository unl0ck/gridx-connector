from __future__ import annotations

import argparse
import json
import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qs, urljoin, urlparse

import requests

DEFAULT_GRANT_TYPE = "http://auth0.com/oauth/grant-type/password-realm"
DEFAULT_AUDIENCE = "my.gridx"
DEFAULT_SCOPE = "email openid offline_access"


@dataclass
class DiscoveryResult:
    login_url: str | None
    client_ids: list[str]
    realms: list[str]
    scopes: list[str]
    audiences: list[str]


def _uniq(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        clean = value.strip()
        if clean and clean not in seen:
            seen.add(clean)
            out.append(clean)
    return out


def _extract_js_urls(html: str, base_url: str) -> list[str]:
    srcs = re.findall(r"<script[^>]+src=[\"']([^\"']+)[\"']", html, flags=re.IGNORECASE)
    return _uniq(urljoin(base_url, src) for src in srcs)


def _extract_from_text(text: str) -> dict[str, list[str]]:
    patterns = {
        "client_id": [
            r"client_id[\"']?\s*[:=]\s*[\"']([A-Za-z0-9_-]{8,})[\"']",
            r"clientId[\"']?\s*[:=]\s*[\"']([A-Za-z0-9_-]{8,})[\"']",
            r"[?&]client_id=([A-Za-z0-9_-]{8,})",
        ],
        "realm": [
            r"realm[\"']?\s*[:=]\s*[\"']([A-Za-z0-9_.-]{3,})[\"']",
            r"connection[\"']?\s*[:=]\s*[\"']([A-Za-z0-9_.-]{3,})[\"']",
            r"databaseConnection[\"']?\s*[:=]\s*[\"']([A-Za-z0-9_.-]{3,})[\"']",
        ],
        "scope": [
            r"scope[\"']?\s*[:=]\s*[\"']([^\"']*openid[^\"']*)[\"']",
            r"[?&]scope=([^&\"']*openid[^&\"']*)",
        ],
        "audience": [
            r"audience[\"']?\s*[:=]\s*[\"']([A-Za-z0-9_.:/-]+)[\"']",
            r"[?&]audience=([A-Za-z0-9_.:/-]+)",
        ],
        "token_url": [
            r"(https?://[^\"']+/oauth/token)",
            r"(https?://[^\"']+auth0\.com/oauth/token)",
        ],
    }

    results: dict[str, list[str]] = {k: [] for k in patterns}
    for key, regexes in patterns.items():
        for regex in regexes:
            results[key].extend(re.findall(regex, text, flags=re.IGNORECASE))

    for key in results:
        results[key] = _uniq(results[key])
    return results


def _extract_from_url(url: str) -> dict[str, list[str]]:
    try:
        parsed = urlparse(url)
    except ValueError:
        return {
            "client_id": [],
            "realm": [],
            "scope": [],
            "audience": [],
        }
    q = parse_qs(parsed.query)
    return {
        "client_id": _uniq(q.get("client_id", [])),
        "realm": _uniq(q.get("realm", []) + q.get("connection", [])),
        "scope": _uniq(q.get("scope", [])),
        "audience": _uniq(q.get("audience", [])),
    }


def discover(site_url: str, timeout: float = 15.0, max_scripts: int = 25) -> DiscoveryResult:
    session = requests.Session()
    session.headers.update({"User-Agent": "gridx-connector oauth-discovery/1.0"})

    response = session.get(site_url, timeout=timeout)
    response.raise_for_status()
    html = response.text

    script_urls = _extract_js_urls(html, base_url=site_url)[:max_scripts]
    all_texts = [html]

    for script_url in script_urls:
        try:
            script_response = session.get(script_url, timeout=timeout)
            if script_response.ok and script_response.text:
                all_texts.append(script_response.text)
        except requests.RequestException:
            continue

    aggregated = {
        "client_id": [],
        "realm": [],
        "scope": [],
        "audience": [],
        "token_url": [],
    }

    for text in all_texts:
        hit = _extract_from_text(text)
        for key in aggregated:
            aggregated[key].extend(hit[key])

    # Also parse query parameters from any URLs embedded in HTML/JS.
    url_candidates = re.findall(r"https?://[^\s\"'<>]+", "\n".join(all_texts))
    for found_url in url_candidates:
        qp = _extract_from_url(found_url)
        aggregated["client_id"].extend(qp["client_id"])
        aggregated["realm"].extend(qp["realm"])
        aggregated["scope"].extend(qp["scope"])
        aggregated["audience"].extend(qp["audience"])

    client_ids = _uniq(aggregated["client_id"])
    realms = _uniq(aggregated["realm"])
    scopes = _uniq(aggregated["scope"])
    audiences = _uniq(aggregated["audience"])
    token_urls = _uniq(aggregated["token_url"])

    login_url = token_urls[0] if token_urls else None
    if not login_url:
        auth0_domains = re.findall(r"https?://[A-Za-z0-9.-]*auth0\.com", "\n".join(all_texts), flags=re.IGNORECASE)
        auth0_domains = _uniq(auth0_domains)
        if auth0_domains:
            login_url = auth0_domains[0].rstrip("/") + "/oauth/token"

    return DiscoveryResult(
        login_url=login_url,
        client_ids=client_ids,
        realms=realms,
        scopes=scopes,
        audiences=audiences,
    )


def build_config(
    *,
    username: str,
    password: str,
    login_url: str,
    client_id: str,
    realm: str,
    audience: str,
    scope: str,
) -> dict:
    return {
        "$schema": "./config.schema.json",
        "urls": {
            "login": login_url,
        },
        "login": {
            "grant_type": DEFAULT_GRANT_TYPE,
            "username": username,
            "password": password,
            "audience": audience,
            "client_id": client_id,
            "scope": scope,
            "realm": realm,
            "client_secret": "",
        },
    }


def validate_login(config: dict, timeout: float = 20.0) -> tuple[bool, str]:
    payload = config["login"].copy()
    login_url = config["urls"]["login"]

    try:
        response = requests.post(login_url, data=payload, timeout=timeout)
    except requests.RequestException as exc:
        return False, f"Request failed: {exc}"

    if response.ok:
        try:
            data = response.json()
        except ValueError:
            data = {}
        if "id_token" in data or "access_token" in data:
            return True, "OAuth token exchange succeeded."
        return False, "Request succeeded but no access/id token in response."

    try:
        error_payload = response.json()
    except ValueError:
        error_payload = {"error": response.text[:300]}
    return False, f"HTTP {response.status_code}: {json.dumps(error_payload)}"


def redact_credentials(config: dict) -> dict:
    redacted = json.loads(json.dumps(config))
    redacted["login"]["username"] = "your@email.com"
    redacted["login"]["password"] = "yourpassword"
    return redacted


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Discover OAuth fields (client_id, realm, scope, audience) from a gridX "
            "login page and optionally write a config."
        )
    )
    parser.add_argument("--site-url", required=True, help="Login/home page URL, e.g. https://eon.gridx.de")
    parser.add_argument("-u", "--username", help="Account username/email (optional, needed for validation/config).")
    parser.add_argument("-p", "--password", help="Account password (optional, needed for validation/config).")
    parser.add_argument("--output", help="Optional output JSON file path for generated config.")
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Attempt OAuth token call with discovered parameters (requires username + password).",
    )
    parser.add_argument(
        "--include-credentials",
        action="store_true",
        help="If --output is set, include username/password in saved file (default: redact).",
    )
    args = parser.parse_args()

    result = discover(args.site_url)

    summary = {
        "site_url": args.site_url,
        "discovered": {
            "login_url": result.login_url,
            "client_id_candidates": result.client_ids,
            "realm_candidates": result.realms,
            "scope_candidates": result.scopes,
            "audience_candidates": result.audiences,
        },
    }

    print(json.dumps(summary, indent=2))

    if args.output:
        missing = []
        if not args.username:
            missing.append("--username")
        if not args.password:
            missing.append("--password")
        if not result.login_url:
            missing.append("discoverable login_url")
        if not result.client_ids:
            missing.append("discoverable client_id")
        if not result.realms:
            missing.append("discoverable realm")

        if missing:
            raise SystemExit(f"Cannot write config. Missing: {', '.join(missing)}")

        config = build_config(
            username=args.username,
            password=args.password,
            login_url=result.login_url,
            client_id=result.client_ids[0],
            realm=result.realms[0],
            audience=result.audiences[0] if result.audiences else DEFAULT_AUDIENCE,
            scope=result.scopes[0] if result.scopes else DEFAULT_SCOPE,
        )

        if args.validate:
            ok, message = validate_login(config)
            print(f"validation: {message}")
            if not ok:
                raise SystemExit(2)

        to_write = config if args.include_credentials else redact_credentials(config)
        out_path = Path(args.output)
        out_path.write_text(json.dumps(to_write, indent=2))
        print(f"config written: {out_path}")


if __name__ == "__main__":
    main()
