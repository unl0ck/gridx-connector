from __future__ import annotations

import asyncio
import json
import logging
import os
import time
from typing import Any
from uuid import UUID

import httpx

from gridx_connector_api import AuthenticatedClient
from gridx_connector_api.api.system.get_systems import asyncio_detailed as _get_systems_async
from gridx_connector_api.api.system.get_systems_system_id_historical import asyncio_detailed as _get_historical_async
from gridx_connector_api.api.system.get_systems_system_id_live import asyncio_detailed as _get_live_async
from gridx_connector_api.models.get_systems_system_id_historical_resolution import (
    GetSystemsSystemIDHistoricalResolution,
)

# Base URL for all gridX REST API calls — does not change per OEM.
_API_BASE_URL = "https://api.gridx.de"

_AUTH_STATUS_CODES = (401, 403)


class AsyncGridboxConnector:
    """Async high-level client for the gridX energy platform."""

    gateways: list[str]
    token: dict[str, Any]
    config: dict[str, Any]
    username: str
    password: str
    logger: logging.Logger
    _api_client: AuthenticatedClient | None
    _httpx_client: httpx.AsyncClient | None
    _owns_httpx_client: bool
    _initialized: bool
    _token_refresh_count: int

    def __init__(
        self,
        config: dict[str, Any],
        logger: logging.Logger | None = None,
        httpx_client: httpx.AsyncClient | None = None,
        owns_httpx_client: bool = False,
    ) -> None:
        if logger:
            self.logger = logger
        else:
            self.init_logging()
        self.config = config
        self.login_url: str = config["urls"]["login"]
        self.login_body: dict[str, str] = config["login"]
        # GRIDX_-prefixed to avoid clashing with the generic USERNAME variable
        # that login shells and Windows set for the current OS user.
        self.username = os.getenv("GRIDX_USERNAME", self.login_body["username"])
        self.password = os.getenv("GRIDX_PASSWORD", self.login_body["password"])
        self.gateways = []
        self.token = {}
        self._api_client = None
        self._httpx_client = httpx_client
        self._owns_httpx_client = owns_httpx_client
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
    ) -> AsyncGridboxConnector:
        connector = cls(
            config=config,
            logger=logger,
            httpx_client=httpx_client,
            owns_httpx_client=owns_httpx_client,
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
            await self.get_gateway_id()
            self._initialized = True

            elapsed = time.perf_counter() - started
            self.logger.info(
                "Async connector initialized in %.2fs (%d systems discovered, %d token fetches).",
                elapsed,
                len(self.gateways),
                self._token_refresh_count,
            )

    def init_logging(self) -> None:
        # Never attach handlers here: libraries must leave handler setup to the
        # application, otherwise embedding apps (e.g. Home Assistant) get
        # duplicate log output. Records propagate to the root logger.
        self.logger = logging.getLogger(__name__)

    def set_loglevel(self, loglevel: str) -> None:
        self.logger.setLevel(logging.getLevelName(loglevel))

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

        if self._httpx_client is not None:
            response = await self._httpx_client.post(self.login_url, data=payload)
            response.raise_for_status()
            token = response.json()
        else:
            async with httpx.AsyncClient() as client:
                response = await client.post(self.login_url, data=payload)
                response.raise_for_status()
                token = response.json()

        expires_at = token.get("expires_at")
        if expires_at is None and token.get("expires_in") is not None:
            token["expires_at"] = time.time() + float(token["expires_in"])

        bearer = token.get("id_token") or token.get("access_token")
        if not bearer:
            raise RuntimeError("Token response did not contain id_token or access_token")

        self.token = token
        self._api_client = AuthenticatedClient(
            base_url=_API_BASE_URL,
            token=bearer,
            raise_on_unexpected_status=False,
        )

        if self._httpx_client is not None:
            # Reuse injected client for API calls and update auth header on refresh.
            auth_value = f"{self._api_client.prefix} {self._api_client.token}"
            self._httpx_client.headers[self._api_client.auth_header_name] = auth_value
            self._api_client.set_async_httpx_client(self._httpx_client)

        if token.get("expires_at"):
            ttl_seconds = max(0, int(float(token["expires_at"]) - time.time()))
            self.logger.debug("Token acquired successfully (expires in %ss).", ttl_seconds)

    async def ensure_valid_token(self) -> None:
        expires_at = self.token.get("expires_at")
        if expires_at is not None and expires_at >= time.time() and self._api_client is not None:
            ttl_seconds = max(0, int(float(expires_at) - time.time()))
            self.logger.debug("Token is still valid for %ss; skipping refresh.", ttl_seconds)
            return

        async with self._token_lock:
            expires_at = self.token.get("expires_at")
            if expires_at is not None and expires_at >= time.time() and self._api_client is not None:
                ttl_seconds = max(0, int(float(expires_at) - time.time()))
                self.logger.debug("Token was refreshed by another task (%ss remaining).", ttl_seconds)
                return

            if expires_at is None:
                reason = "missing-token"
            else:
                reason = "expired-token"

            self.logger.info("Token invalid (%s), refreshing now.", reason)
            await self.get_new_token(reason=reason)

    async def _get_api_client(self) -> AuthenticatedClient:
        await self.ensure_valid_token()
        assert self._api_client is not None
        return self._api_client

    async def get_gateway_id(self) -> None:
        """Discover the systems linked to the account.

        Raises:
            PermissionError: If the API rejects the credentials (401/403).
            RuntimeError: If the API returns any other non-200 status.

        Network errors from the underlying HTTP client propagate unchanged.
        """
        self.gateways.clear()
        response = await _get_systems_async(client=await self._get_api_client())
        status = response.status_code.value
        if status in _AUTH_STATUS_CODES:
            raise PermissionError(f"System discovery rejected with HTTP {status}")
        if status != 200:
            raise RuntimeError(f"System discovery failed with HTTP {status}")
        systems = json.loads(response.content)
        if isinstance(systems, list):
            for system in systems:
                system_id = system.get("id")
                if system_id:
                    self.gateways.append(str(system_id))
        self.logger.debug("Discovered %d systems.", len(self.gateways))

    def get_gateways(self) -> list[str]:
        return self.gateways

    def _collect_results(
        self,
        results: list[dict[str, Any] | None | BaseException],
        what: str,
    ) -> list[dict[str, Any]]:
        """Collect per-system results, tolerating partial failures.

        Authentication errors always propagate so callers can re-authenticate.
        Other errors are tolerated as long as at least one system succeeded;
        if every system failed, the first error is raised.
        """
        parsed: list[dict[str, Any]] = []
        errors: list[BaseException] = []
        for result in results:
            if isinstance(result, PermissionError):
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

    async def retrieve_live_data_by_id(self, system_id: str) -> dict[str, Any] | None:
        """Fetch live data for one system.

        Raises:
            PermissionError: If the API rejects the credentials (401/403).

        Other non-200 statuses return None; network errors propagate unchanged.
        """
        response = await _get_live_async(system_id=UUID(system_id), client=await self._get_api_client())
        status = response.status_code.value
        if status in _AUTH_STATUS_CODES:
            raise PermissionError(f"Live data request for system {system_id} rejected with HTTP {status}")
        if status != 200:
            self.logger.warning(f"Status Code {status} for system {system_id}")
            return None
        return json.loads(response.content)

    async def retrieve_live_data(self) -> list[dict[str, Any]]:
        tasks = [self.retrieve_live_data_by_id(system_id) for system_id in self.gateways]
        if not tasks:
            return []
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return self._collect_results(results, "live data")

    async def retrieve_historical_data_by_id(
        self,
        system_id: str,
        start: str,
        end: str,
        resolution: str = "15m",
    ) -> dict[str, Any] | None:
        """Fetch historical data for one system.

        Raises:
            PermissionError: If the API rejects the credentials (401/403).

        Other non-200 statuses return None; network errors propagate unchanged.
        """
        interval = f"{start}/{end}"
        try:
            res_enum = GetSystemsSystemIDHistoricalResolution(resolution)
        except ValueError:
            self.logger.warning(f"Unknown resolution '{resolution}', using default '15m'")
            res_enum = GetSystemsSystemIDHistoricalResolution.VALUE_0
        response = await _get_historical_async(
            system_id=UUID(system_id),
            client=await self._get_api_client(),
            interval=interval,
            resolution=res_enum,
        )
        status = response.status_code.value
        if status in _AUTH_STATUS_CODES:
            raise PermissionError(f"Historical data request for system {system_id} rejected with HTTP {status}")
        if status != 200:
            self.logger.warning(f"Status Code {status} for system {system_id}")
            return None
        return json.loads(response.content)

    async def retrieve_historical_data(
        self,
        start: str,
        end: str,
        resolution: str = "15m",
    ) -> list[dict[str, Any]]:
        tasks = [
            self.retrieve_historical_data_by_id(system_id=system_id, start=start, end=end, resolution=resolution)
            for system_id in self.gateways
        ]
        if not tasks:
            return []
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return self._collect_results(results, "historical data")

    async def close(self) -> None:
        if self._httpx_client is not None and self._owns_httpx_client:
            self.logger.debug("Closing owned injected async HTTP client.")
            await self._httpx_client.aclose()
            return

        if self._api_client is None:
            return
        self.logger.debug("Closing async API client.")
        await self._api_client.get_async_httpx_client().aclose()

    async def __aenter__(self) -> AsyncGridboxConnector:
        await self.initialize()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()
