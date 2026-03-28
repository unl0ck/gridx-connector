from __future__ import annotations

import argparse
import asyncio
import json
import sys
import warnings
from importlib.resources import files
from pathlib import Path
from typing import Any

from .async_connector import AsyncGridboxConnector
from .GridboxConnector import GridboxConnector
from .supported_oem import SupportedOEM

_ALL_OEMS: list[str] = ["eon-home"]

# OAuth2 defaults shared across all known gridX realms.
_DEFAULT_GRANT_TYPE = "http://auth0.com/oauth/grant-type/password-realm"
_DEFAULT_AUDIENCE = "my.gridx"
_DEFAULT_SCOPE = "email openid offline_access"


def _load_oem_config(oem: str, username: str, password: str) -> dict[str, Any]:
    """Load a bundled OEM config and inject credentials."""
    if oem == "viessmann":
        warnings.warn(
            "The Viessmann realm was shut down at end of 2025. Support for 'viessmann' OEM is deprecated.",
            DeprecationWarning,
            stacklevel=3,
        )
    config_file = files("gridx_connector").joinpath("config", f"{oem}.config.json")
    with open(config_file) as fh:
        config: dict[str, Any] = json.load(fh)
    config["login"]["username"] = username
    config["login"]["password"] = password
    return config


def _build_config(
    username: str,
    password: str,
    login_url: str,
    client_id: str,
    realm: str,
    audience: str = _DEFAULT_AUDIENCE,
) -> dict[str, Any]:
    """Build a config dict from individual parameters (no config file needed)."""
    return {
        "urls": {"login": login_url},
        "login": {
            "grant_type": _DEFAULT_GRANT_TYPE,
            "username": username,
            "password": password,
            "audience": audience,
            "client_id": client_id,
            "scope": _DEFAULT_SCOPE,
            "realm": realm,
            "client_secret": "",
        },
    }


def retrieve_live_data(username: str, password: str, oem: str = SupportedOEM.EON_HOME) -> list[dict[str, Any]]:
    config = _load_oem_config(oem, username, password)
    connector = GridboxConnector(config)
    return connector.retrieve_live_data()


async def _retrieve_live_data_async(config: dict[str, Any]) -> list[dict[str, Any]]:
    async with AsyncGridboxConnector(config) as connector:
        return await connector.retrieve_live_data()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Retrieve live data from GridX Gridbox.",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # Credentials (always required)
    parser.add_argument("-u", "--username", required=True, help="Login username (e-mail).")
    parser.add_argument("-p", "--password", required=True, help="Login password.")

    # Config source — either a bundled OEM name OR a custom login URL
    source = parser.add_mutually_exclusive_group()
    source.add_argument(
        "-o",
        "--oem",
        default=SupportedOEM.EON_HOME,
        choices=_ALL_OEMS,
        help="Bundled OEM config to use (default: eon-home).",
    )
    source.add_argument(
        "--login-url",
        metavar="URL",
        help=(
            "OAuth2 token endpoint, e.g.\n  https://gridx.eu.auth0.com/oauth/token\nRequires --client-id and --realm."
        ),
    )
    source.add_argument(
        "--config",
        metavar="FILE",
        help="Path to a custom OEM config JSON file.",
    )

    # Extra parameters only needed together with --login-url
    parser.add_argument("--client-id", metavar="ID", help="OAuth2 client ID (required with --login-url).")
    parser.add_argument("--realm", help="Auth0 realm (required with --login-url).")
    parser.add_argument(
        "--audience",
        default=_DEFAULT_AUDIENCE,
        help=f"OAuth2 audience (default: {_DEFAULT_AUDIENCE}).",
    )

    # Optional: persist the generated config
    parser.add_argument(
        "--save-config",
        metavar="FILE",
        help="Save the resolved config (without credentials) to a JSON file for reuse.",
    )
    parser.add_argument(
        "--async",
        action="store_true",
        dest="use_async",
        help="Use asynchronous retrieval (useful for accounts with many systems).",
    )

    args = parser.parse_args()

    # Resolve config
    if args.login_url:
        missing = [f for f, v in [("--client-id", args.client_id), ("--realm", args.realm)] if not v]
        if missing:
            parser.error(f"--login-url requires: {', '.join(missing)}")
        config = _build_config(
            username=args.username,
            password=args.password,
            login_url=args.login_url,
            client_id=args.client_id,
            realm=args.realm,
            audience=args.audience,
        )
    elif args.config:
        config_path = Path(args.config)
        if not config_path.is_file():
            parser.error(f"Config file not found: {args.config}")
        with open(config_path) as fh:
            config = json.load(fh)
        config["login"]["username"] = args.username
        config["login"]["password"] = args.password
    else:
        config = _load_oem_config(args.oem, args.username, args.password)

    # Optionally save config (credentials stripped)
    if args.save_config:
        save_path = Path(args.save_config)
        saveable = json.loads(json.dumps(config))
        saveable["login"]["username"] = "your@email.com"
        saveable["login"]["password"] = "yourpassword"
        save_path.write_text(json.dumps(saveable, indent=2))
        print(f"Config saved to {save_path}", file=sys.stderr)

    if args.use_async:
        live_data = asyncio.run(_retrieve_live_data_async(config))
    else:
        connector = GridboxConnector(config)
        live_data = connector.retrieve_live_data()
    print(json.dumps(live_data, indent=2))


if __name__ == "__main__":
    main()
