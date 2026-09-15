from __future__ import annotations

import asyncio
import logging
import os
import time
from collections.abc import Awaitable, Callable, Iterable
from dataclasses import dataclass, field
from typing import Any

import httpx

from .exceptions import GridXAuthenticationError, GridXConnectionError, GridXError, GridXResponseError
from .oem import API_BASE_URL

# Kept for backwards compatibility; use ``gridx_connector.oem.API_BASE_URL``.
_API_BASE_URL = API_BASE_URL

_AUTH_STATUS_CODES = (401, 403)
_DEFAULT_TIMEOUT = 20.0


@dataclass(frozen=True)
class GridXSystem:
    """A system (gridBox plus appliances) discovered for the account."""

    id: str
    name: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    serial_number: str | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False, compare=False)

    @classmethod
    def from_api(cls, system: dict[str, Any]) -> GridXSystem:
        gateways = system.get("gateways") or []
        gateway = gateways[0] if gateways and isinstance(gateways[0], dict) else {}
        return cls(
            id=str(system["id"]),
            name=system.get("name") or None,
            manufacturer=gateway.get("manufacturer") or None,
            model=gateway.get("model") or None,
            serial_number=gateway.get("serialnumber") or None,
            raw=system,
        )


class AsyncGridboxConnector:
    """Async high-level client for the gridX energy platform.

    Errors are reported through the :mod:`gridx_connector.exceptions`
    hierarchy: :class:`GridXAuthenticationError` for rejected credentials or
    tokens, :class:`GridXConnectionError` for network problems and
    :class:`GridXResponseError` for unexpected HTTP statuses or payloads.

    Credentials are taken from ``config["login"]``. The environment variables
    ``GRIDX_USERNAME`` / ``GRIDX_PASSWORD`` are only consulted when the config
    does not provide a value.

    The bearer token is sent per request; an injected ``httpx_client`` is never
    modified, so it may be shared with other consumers.
    """

    systems: dict[str, GridXSystem]
    gateways: list[str]
    token: dict[str, Any]
    config: dict[str, Any]
    username: str
    password: str
    logger: logging.Logger

    def __init__(
        self,
        config: dict[str, Any],
        logger: logging.Logger | None = None,
        httpx_client: httpx.AsyncClient | None = None,
        owns_httpx_client: bool = False,
        timeout: float | None = None,
    ) -> None:
        # Never attach handlers here: libraries must leave handler setup to the
        # application, otherwise embedding apps (e.g. Home Assistant) get
        # duplicate log output. Records propagate to the root logger.
        self.logger = logger or logging.getLogger(__name__)
        self.config = config
        self.login_url: str = config["urls"]["login"]
        self.login_body: dict[str, str] = config["login"]
        # Explicit configuration wins; the GRIDX_-prefixed environment
        # variables only fill in values the config leaves empty.
        self.username = self.login_body.get("username") or os.getenv("GRIDX_USERNAME", "")
        self.password = self.login_body.get("password") or os.getenv("GRIDX_PASSWORD", "")
        self.systems = {}
        self.gateways = []
        self.token = {}
        self._httpx_client = httpx_client
        # A client we create ourselves is always ours to close.
        self._owns_httpx_client = owns_httpx_client or httpx_client is None
        self._timeout = timeout
        self._active_token_type = "access_token"
        self._initialized = False
        self._token_refresh_count = 0
        self._token_lock = asyncio.Lock()
        self._init_lock = asyncio.Lock()

    @classmethod
    async def create(
        cls,
        config: dict[str, Any],
        logger: logging.Logger | None = None,
        httpx_client: httpx.AsyncClient | None = None,
        owns_httpx_client: bool = False,
        timeout: float | None = None,
    ) -> AsyncGridboxConnector:
        """Create a connector, authenticate and discover the account's systems."""
        connector = cls(
            config=config,
            logger=logger,
            httpx_client=httpx_client,
            owns_httpx_client=owns_httpx_client,
            timeout=timeout,
        )
        await connector.initialize()
        return connector

    async def initialize(self, force: bool = False) -> None:
        async with self._init_lock:
            if self._initialized and not force:
                self.logger.debug("Initialization skipped: connector already initialized.")
                return

            started = time.perf_counter()
            reason = "forced-reinitialize" if force and self._initialized else "initialization"
            await self.get_new_token(reason=reason)
            await self.discover_systems()
            self._initialized = True

            elapsed = time.perf_counter() - started
            self.logger.info(
                "Async connector initialized in %.2fs (%d systems discovered, %d token fetches).",
                elapsed,
                len(self.systems),
                self._token_refresh_count,
            )

    def init_logging(self) -> None:
        self.logger = logging.getLogger(__name__)

    def set_loglevel(self, loglevel: str) -> None:
        self.logger.setLevel(logging.getLevelName(loglevel))

    # ------------------------------------------------------------------ HTTP

    @property
    def _client(self) -> httpx.AsyncClient:
        if self._httpx_client is None:
            self._httpx_client = httpx.AsyncClient(timeout=self._timeout or _DEFAULT_TIMEOUT)
        return self._httpx_client

    async def _request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        if self._timeout is not None:
            kwargs.setdefault("timeout", self._timeout)
        try:
            return await self._client.request(method, url, **kwargs)
        except httpx.HTTPError as err:
            raise GridXConnectionError(f"Request to {url} failed: {err}") from err

    @staticmethod
    def _json(response: httpx.Response, what: str) -> Any:
        try:
            return response.json()
        except ValueError as err:
            raise GridXResponseError(f"{what} returned malformed JSON", response.status_code) from err

    async def _api_get(self, path: str, what: str, **kwargs: Any) -> Any:
        """GET ``path`` with a valid bearer token and return the parsed JSON body."""
        await self.ensure_valid_token()
        url = f"{API_BASE_URL}{path}"
        response = await self._request("GET", url, headers=self._auth_headers(), **kwargs)
        if response.status_code in _AUTH_STATUS_CODES and self._switch_to_id_token():
            self.logger.warning("Access token rejected; retrying request with ID token.")
            response = await self._request("GET", url, headers=self._auth_headers(), **kwargs)
        if response.status_code in _AUTH_STATUS_CODES:
            raise GridXAuthenticationError(f"{what} rejected with HTTP {response.status_code}")
        if response.status_code != 200:
            raise GridXResponseError(f"{what} failed with HTTP {response.status_code}", response.status_code)
        return self._json(response, what)

    def _auth_headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.token[self._active_token_type]}"}

    def _switch_to_id_token(self) -> bool:
        """Fall back to the ID token once if the access token is not accepted."""
        if self._active_token_type == "access_token" and self.token.get("id_token"):
            self._active_token_type = "id_token"
            return True
        return False

    # ----------------------------------------------------------------- token

    async def get_new_token(self, reason: str = "refresh") -> None:
        self._token_refresh_count += 1
        self.logger.info(
            "Fetching OAuth token (%s, attempt #%d, realm=%s)",
            reason,
            self._token_refresh_count,
            self.login_body.get("realm", "unknown"),
        )

        payload = {
            "username": self.username,
            "password": self.password,
            "grant_type": self.login_body["grant_type"],
            "audience": self.login_body["audience"],
            "realm": self.login_body["realm"],
            "scope": self.login_body["scope"],
            "client_id": self.login_body["client_id"],
            "client_secret": self.login_body.get("client_secret", ""),
        }

        response = await self._request("POST", self.login_url, data=payload)
        if response.status_code in _AUTH_STATUS_CODES:
            raise GridXAuthenticationError(f"Token request rejected with HTTP {response.status_code}")
        if not response.is_success:
            raise GridXResponseError(f"Token request failed with HTTP {response.status_code}", response.status_code)
        token = self._json(response, "Token request")

        if token.get("expires_at") is None and token.get("expires_in") is not None:
            token["expires_at"] = time.time() + float(token["expires_in"])

        if token.get("access_token"):
            self._active_token_type = "access_token"
        elif token.get("id_token"):
            self._active_token_type = "id_token"
        else:
            raise GridXResponseError("Token response did not contain access_token or id_token", response.status_code)
        self.token = token

        if token.get("expires_at"):
            ttl_seconds = max(0, int(float(token["expires_at"]) - time.time()))
            self.logger.debug("Token acquired successfully (expires in %ss).", ttl_seconds)

    def _token_is_valid(self) -> bool:
        expires_at = self.token.get("expires_at")
        return bool(self.token.get(self._active_token_type)) and expires_at is not None and expires_at >= time.time()

    async def ensure_valid_token(self) -> None:
        if self._token_is_valid():
            return

        async with self._token_lock:
            if self._token_is_valid():
                self.logger.debug("Token was refreshed by another task.")
                return
            reason = "missing-token" if not self.token else "expired-token"
            self.logger.info("Token invalid (%s), refreshing now.", reason)
            await self.get_new_token(reason=reason)

    # --------------------------------------------------------------- systems

    async def discover_systems(self) -> dict[str, GridXSystem]:
        """Fetch the systems linked to the account and remember them.

        Raises:
            GridXAuthenticationError: If the API rejects the credentials.
            GridXConnectionError: If the API cannot be reached.
            GridXResponseError: If the API returns any other non-200 status.
        """
        systems = await self._api_get("/systems", "System discovery")
        discovered: dict[str, GridXSystem] = {}
        if isinstance(systems, list):
            for system in systems:
                if isinstance(system, dict) and system.get("id"):
                    parsed = GridXSystem.from_api(system)
                    discovered[parsed.id] = parsed
        self.systems = discovered
        self.gateways = list(discovered)
        self.logger.debug("Discovered %d systems.", len(discovered))
        return discovered

    async def get_gateway_id(self) -> None:
        """Deprecated alias of :meth:`discover_systems`."""
        await self.discover_systems()

    def get_gateways(self) -> list[str]:
        return self.gateways

    async def _gather_strict(
        self,
        system_ids: Iterable[str] | None,
        fetch: Callable[[str], Awaitable[dict[str, Any]]],
        what: str,
    ) -> dict[str, dict[str, Any]]:
        """Run ``fetch`` for every system; raise if any system fails."""
        ids = list(system_ids) if system_ids is not None else list(self.systems)
        results = await asyncio.gather(*(fetch(system_id) for system_id in ids), return_exceptions=True)
        data: dict[str, dict[str, Any]] = {}
        errors: list[tuple[str, BaseException]] = []
        for system_id, result in zip(ids, results, strict=True):
            if isinstance(result, BaseException):
                errors.append((system_id, result))
            else:
                data[system_id] = result
        if not errors:
            return data
        for _, error in errors:
            if isinstance(error, GridXAuthenticationError):
                raise error
        failed = ", ".join(system_id for system_id, _ in errors)
        first = errors[0][1]
        if isinstance(first, GridXResponseError):
            raise GridXResponseError(f"{what} failed for system(s) {failed}: {first}", first.status_code) from first
        if isinstance(first, GridXError):
            raise type(first)(f"{what} failed for system(s) {failed}: {first}") from first
        raise first

    async def _gather_tolerant(
        self,
        fetch: Callable[[str], Awaitable[dict[str, Any] | None]],
        what: str,
    ) -> list[dict[str, Any]]:
        """Run ``fetch`` for every system, tolerating partial failures.

        Authentication errors always propagate. Other errors are tolerated as
        long as at least one system succeeded; if every system failed, the
        first error is raised.
        """
        if not self.systems:
            return []
        results = await asyncio.gather(*(fetch(system_id) for system_id in self.systems), return_exceptions=True)
        parsed: list[dict[str, Any]] = []
        errors: list[BaseException] = []
        for result in results:
            if isinstance(result, GridXAuthenticationError):
                raise result
            if isinstance(result, BaseException):
                errors.append(result)
                continue
            if result is not None:
                parsed.append(result)
        if errors and not parsed:
            raise errors[0]
        for error in errors:
            self.logger.warning("Ignoring %s failure for one system: %s", what, error)
        return parsed

    # ------------------------------------------------------------- live data

    async def get_live_data_by_id(self, system_id: str) -> dict[str, Any]:
        """Fetch the live snapshot of one system; raises on any failure."""
        return await self._api_get(f"/systems/{system_id}/live", f"Live data request for system {system_id}")

    async def get_live_data(self, system_ids: Iterable[str] | None = None) -> dict[str, dict[str, Any]]:
        """Fetch live snapshots keyed by system id.

        Defaults to every discovered system. Unlike :meth:`retrieve_live_data`
        this does not tolerate partial failures: if any system fails, the
        error is raised and no partial result is returned.
        """
        return await self._gather_strict(system_ids, self.get_live_data_by_id, "Live data request")

    async def retrieve_live_data_by_id(self, system_id: str) -> dict[str, Any] | None:
        """Fetch live data for one system, returning ``None`` on non-200 statuses.

        Raises:
            GridXAuthenticationError: If the API rejects the credentials.
            GridXConnectionError: If the API cannot be reached.
        """
        try:
            return await self.get_live_data_by_id(system_id)
        except GridXResponseError as err:
            self.logger.warning("Status Code %s for system %s", err.status_code, system_id)
            return None

    async def retrieve_live_data(self) -> list[dict[str, Any]]:
        """Fetch live data for all systems, tolerating partial failures.

        Prefer :meth:`get_live_data` when partial results are not acceptable.
        """
        return await self._gather_tolerant(self.retrieve_live_data_by_id, "live data")

    # ------------------------------------------------------- historical data

    async def get_historical_data_by_id(
        self,
        system_id: str,
        start: str,
        end: str,
        resolution: str = "15m",
    ) -> dict[str, Any]:
        """Fetch historical data for one system; raises on any failure."""
        return await self._api_get(
            f"/systems/{system_id}/historical",
            f"Historical data request for system {system_id}",
            params={"interval": f"{start}/{end}", "resolution": resolution},
        )

    async def get_historical_data(
        self,
        start: str,
        end: str,
        resolution: str = "15m",
        system_ids: Iterable[str] | None = None,
    ) -> dict[str, dict[str, Any]]:
        """Fetch historical data keyed by system id; raises if any system fails."""

        async def fetch(system_id: str) -> dict[str, Any]:
            return await self.get_historical_data_by_id(system_id, start, end, resolution)

        return await self._gather_strict(system_ids, fetch, "Historical data request")

    async def retrieve_historical_data_by_id(
        self,
        system_id: str,
        start: str,
        end: str,
        resolution: str = "15m",
    ) -> dict[str, Any] | None:
        """Fetch historical data for one system, returning ``None`` on non-200 statuses."""
        try:
            return await self.get_historical_data_by_id(system_id, start, end, resolution)
        except GridXResponseError as err:
            self.logger.warning("Status Code %s for system %s", err.status_code, system_id)
            return None

    async def retrieve_historical_data(
        self,
        start: str,
        end: str,
        resolution: str = "15m",
    ) -> list[dict[str, Any]]:
        """Fetch historical data for all systems, tolerating partial failures."""

        async def fetch(system_id: str) -> dict[str, Any] | None:
            return await self.retrieve_historical_data_by_id(system_id, start, end, resolution)

        return await self._gather_tolerant(fetch, "historical data")

    # ------------------------------------------------------------- lifecycle

    async def close(self) -> None:
        if self._httpx_client is not None and self._owns_httpx_client:
            self.logger.debug("Closing owned async HTTP client.")
            await self._httpx_client.aclose()
            self._httpx_client = None

    async def __aenter__(self) -> AsyncGridboxConnector:
        await self.initialize()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()
