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
from gridx_connector_api.api.system.get_systems import asyncio as _get_systems_async
from gridx_connector_api.api.system.get_systems_system_id_historical import asyncio_detailed as _get_historical_async
from gridx_connector_api.api.system.get_systems_system_id_live import asyncio_detailed as _get_live_async
from gridx_connector_api.models.get_systems_system_id_historical_resolution import (
    GetSystemsSystemIDHistoricalResolution,
)

# Base URL for all gridX REST API calls — does not change per OEM.
_API_BASE_URL = "https://api.gridx.de"


class AsyncGridboxConnector:
    """Async high-level client for the gridX energy platform."""

    gateways: list[str]
    token: dict[str, Any]
    config: dict[str, Any]
    username: str
    password: str
    logger: logging.Logger
    _api_client: AuthenticatedClient | None

    def __init__(self, config: dict[str, Any], logger: logging.Logger | None = None) -> None:
        if logger:
            self.logger = logger
        else:
            self.init_logging()
        self.config = config
        self.login_url: str = config["urls"]["login"]
        self.login_body: dict[str, str] = config["login"]
        self.username = os.getenv("USERNAME", self.login_body["username"])
        self.password = os.getenv("PASSWORD", self.login_body["password"])
        self.gateways = []
        self.token = {}
        self._api_client = None
        self._token_lock = asyncio.Lock()

    @classmethod
    async def create(cls, config: dict[str, Any], logger: logging.Logger | None = None) -> AsyncGridboxConnector:
        connector = cls(config=config, logger=logger)
        await connector.initialize()
        return connector

    async def initialize(self) -> None:
        await self.get_new_token()
        await self.get_gateway_id()

    def init_logging(self) -> None:
        self.logger = logging.getLogger(__name__)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s")
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def set_loglevel(self, loglevel: str) -> None:
        self.logger.setLevel(logging.getLevelName(loglevel))

    async def get_new_token(self) -> None:
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
        if token.get("expires_at"):
            self.logger.debug(f"Token expires at {token['expires_at']}")

    async def ensure_valid_token(self) -> None:
        expires_at = self.token.get("expires_at")
        if expires_at is not None and expires_at >= time.time() and self._api_client is not None:
            return

        async with self._token_lock:
            expires_at = self.token.get("expires_at")
            if expires_at is not None and expires_at >= time.time() and self._api_client is not None:
                return
            self.logger.info("Token expired or missing, refreshing...")
            await self.get_new_token()

    async def _get_api_client(self) -> AuthenticatedClient:
        await self.ensure_valid_token()
        assert self._api_client is not None
        return self._api_client

    async def get_gateway_id(self) -> None:
        self.gateways.clear()
        try:
            systems = await _get_systems_async(client=await self._get_api_client())
            if isinstance(systems, list):
                for system in systems:
                    system_id = system.additional_properties.get("id")
                    if system_id:
                        self.gateways.append(str(system_id))
        except Exception as exc:
            self.logger.error(exc)

    def get_gateways(self) -> list[str]:
        return self.gateways

    async def retrieve_live_data_by_id(self, system_id: str) -> dict[str, Any] | None:
        try:
            response = await _get_live_async(system_id=UUID(system_id), client=await self._get_api_client())
            if response.status_code.value != 200:
                self.logger.warning(f"Status Code {response.status_code.value} for system {system_id}")
                return None
            return json.loads(response.content)
        except Exception as exc:
            self.logger.error(exc)
            return None

    async def retrieve_live_data(self) -> list[dict[str, Any]]:
        tasks = [self.retrieve_live_data_by_id(system_id) for system_id in self.gateways]
        if not tasks:
            return []
        results = await asyncio.gather(*tasks, return_exceptions=True)

        parsed: list[dict[str, Any]] = []
        for result in results:
            if isinstance(result, Exception):
                self.logger.error(result)
                continue
            if result is not None:
                parsed.append(result)
        return parsed

    async def retrieve_historical_data_by_id(
        self,
        system_id: str,
        start: str,
        end: str,
        resolution: str = "15m",
    ) -> dict[str, Any] | None:
        interval = f"{start}/{end}"
        try:
            res_enum = GetSystemsSystemIDHistoricalResolution(resolution)
        except ValueError:
            self.logger.warning(f"Unknown resolution '{resolution}', using default '15m'")
            res_enum = GetSystemsSystemIDHistoricalResolution.VALUE_0
        try:
            response = await _get_historical_async(
                system_id=UUID(system_id),
                client=await self._get_api_client(),
                interval=interval,
                resolution=res_enum,
            )
            if response.status_code.value != 200:
                self.logger.warning(f"Status Code {response.status_code.value} for system {system_id}")
                return None
            return json.loads(response.content)
        except Exception as exc:
            self.logger.error(exc)
            return None

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

        parsed: list[dict[str, Any]] = []
        for result in results:
            if isinstance(result, Exception):
                self.logger.error(result)
                continue
            if result is not None:
                parsed.append(result)
        return parsed

    async def close(self) -> None:
        if self._api_client is None:
            return
        await self._api_client.get_async_httpx_client().aclose()

    async def __aenter__(self) -> AsyncGridboxConnector:
        await self.initialize()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()
