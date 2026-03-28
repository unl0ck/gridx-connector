from __future__ import annotations

import json
import logging
import os
import time
from typing import Any
from uuid import UUID

from authlib.integrations.requests_client import OAuth2Session

from gridx_connector_api import AuthenticatedClient
from gridx_connector_api.api.system.get_systems import sync as _get_systems
from gridx_connector_api.api.system.get_systems_system_id_historical import sync_detailed as _get_historical
from gridx_connector_api.api.system.get_systems_system_id_live import sync_detailed as _get_live
from gridx_connector_api.models.get_systems_system_id_historical_resolution import (
    GetSystemsSystemIDHistoricalResolution,
)

# Base URL for all gridX REST API calls — does not change per OEM.
_API_BASE_URL = "https://api.gridx.de"


class GridboxConnector:
    """High-level client for the gridX energy platform.

    Handles OAuth2 authentication against Auth0, discovers the caller's
    registered energy systems, and exposes methods to retrieve live and
    historical measurements via the auto-generated ``gridx_connector_api``
    HTTP client.

    Typical usage::

        connector = GridboxConnector(config)
        live  = connector.retrieve_live_data()
        hist  = connector.retrieve_historical_data(
            start="2024-01-01T00:00:00+01:00",
            end="2024-01-02T00:00:00+01:00",
        )
    """

    gateways: list[str]
    token: dict[str, Any]
    client: OAuth2Session
    config: dict[str, Any]
    username: str
    password: str
    logger: logging.Logger
    _api_client: AuthenticatedClient | None

    def __init__(self, config: dict[str, Any], logger: logging.Logger | None = None) -> None:
        """Initialise the connector.

        Reads credentials from ``config["login"]`` but allows the
        ``USERNAME`` / ``PASSWORD`` environment variables to override them
        so that secrets can be injected at runtime without modifying the
        config file.
        """
        if not logger:
            self.init_logging()
        self.config = config
        self.login_url: str = config["urls"]["login"]
        self.login_body: dict[str, str] = config["login"]
        # Env-var overrides take precedence over values in the config file.
        self.username = os.getenv("USERNAME", self.login_body["username"])
        self.password = os.getenv("PASSWORD", self.login_body["password"])
        self.gateways = []  # instance-level list, not shared across instances
        self._api_client = None
        self.init_auth()

    def init_logging(self) -> None:
        self.logger = logging.getLogger(__name__)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s")
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def set_loglevel(self, loglevel: str) -> None:
        self.logger.setLevel(logging.getLevelName(loglevel))

    def get_new_token(self) -> None:
        """Fetch a fresh OAuth2 token from Auth0 and rebuild the API client.

        ``AuthenticatedClient`` is immutable with respect to its bearer token,
        so a new instance must be created every time the token is refreshed.
        """
        self.token = self.client.fetch_token(
            self.login_url,
            username=self.login_body["username"],
            password=self.login_body["password"],
            grant_type=self.login_body["grant_type"],
            audience=self.login_body["audience"],
            realm=self.login_body["realm"],
            scope=self.login_body["scope"],
        )
        # Recreate the httpx-based client with the new id_token as bearer.
        self._api_client = AuthenticatedClient(
            base_url=_API_BASE_URL,
            token=self.token["id_token"],
            raise_on_unexpected_status=False,
        )
        self.logger.debug(f"Token expires at {self.token['expires_at']}")

    def ensure_valid_token(self) -> None:
        """Refresh the token when it has expired or is not yet set."""
        expires_at: float | None = self.token.get("expires_at")
        if expires_at is None or expires_at < time.time():
            self.logger.info("Token expired or missing, refreshing...")
            self.get_new_token()

    def _get_api_client(self) -> AuthenticatedClient:
        """Return a ready-to-use ``AuthenticatedClient``, refreshing if needed.

        All data-retrieval methods call this instead of accessing
        ``self._api_client`` directly so that token expiry is handled
        transparently before every request.
        """
        self.ensure_valid_token()
        assert self._api_client is not None
        return self._api_client

    def init_auth(self) -> None:
        """Create the OAuth2 session, fetch the initial token and load system IDs."""
        client_id: str = self.login_body["client_id"]
        client_secret: str = self.login_body["client_secret"]
        self.client = OAuth2Session(client_id, client_secret, scope=self.login_body["scope"])
        self.get_new_token()
        self.get_gateway_id()

    def get_gateway_id(self) -> None:
        """Populate ``self.gateways`` with the IDs of all registered systems.

        Uses ``GET /systems`` (not ``GET /gateways``) because the systems
        endpoint returns the IDs needed by the live/historical endpoints.
        On failure the method waits 60 s and retries — this guards against
        transient network issues during startup.
        """
        self.gateways.clear()
        try:
            systems = _get_systems(client=self._get_api_client())
            if isinstance(systems, list):
                for system in systems:
                    # The generated model stores extra fields in additional_properties.
                    system_id = system.additional_properties.get("id")
                    if system_id:
                        self.gateways.append(str(system_id))
        except Exception as e:
            self.logger.error(e)
            time.sleep(60)
            self.get_gateway_id()

    def get_gateways(self) -> list[str]:
        """Return the list of system IDs discovered during initialisation."""
        return self.gateways

    def retrieve_live_data_by_id(self, system_id: str) -> dict[str, Any] | None:
        """Fetch the current measurement snapshot for a single system.

        Returns ``None`` on non-200 responses or network errors so that callers
        can skip failing systems without crashing.

        Note: the generated client cannot parse the 200 response of
        ``GET /systems/{systemID}/live`` as a typed model (duplicate schema
        name in the OpenAPI spec), so the raw response bytes are decoded
        manually with ``json.loads``.
        """
        try:
            response = _get_live(system_id=UUID(system_id), client=self._get_api_client())
            if response.status_code.value != 200:
                self.logger.warning(f"Status Code {response.status_code.value} for system {system_id}")
                return None
            # response.content holds the raw JSON bytes; parse them directly.
            return json.loads(response.content)
        except Exception as e:
            self.logger.error(e)
            return None

    def retrieve_live_data(self) -> list[dict[str, Any]]:
        """Fetch live data for all discovered systems.

        Systems that return an error are skipped; the result list may
        therefore be shorter than ``self.gateways``.
        """
        results: list[dict[str, Any]] = []
        for system_id in self.gateways:
            try:
                data = self.retrieve_live_data_by_id(system_id)
                if data is not None:
                    results.append(data)
            except Exception as e:
                self.logger.error(e)
        return results

    def retrieve_historical_data_by_id(
        self, system_id: str, start: str, end: str, resolution: str = "15m"
    ) -> dict[str, Any] | None:
        """Fetch aggregated historical measurements for a single system.

        Args:
            system_id:  UUID string of the target system.
            start:      ISO-8601 timestamp for the start of the interval
                        (e.g. ``"2024-01-01T00:00:00+01:00"``).
            end:        ISO-8601 timestamp for the end of the interval.
            resolution: Aggregation bucket size.  Must be one of
                        ``15m``, ``1h``, ``1d``, ``1w``, ``1M``.
                        Falls back to ``15m`` when an unknown value is given.

        Returns:
            A dict with ``measurements`` (list) and ``total`` keys, or
            ``None`` on error.
        """
        # The API expects an ISO 8601 interval string: "<start>/<end>".
        interval = f"{start}/{end}"
        # Map the human-readable string to the generated enum; fall back to
        # the finest resolution (15m) if the caller passes an unknown value.
        try:
            res_enum = GetSystemsSystemIDHistoricalResolution(resolution)
        except ValueError:
            self.logger.warning(f"Unknown resolution '{resolution}', using default '15m'")
            res_enum = GetSystemsSystemIDHistoricalResolution.VALUE_0
        try:
            response = _get_historical(
                system_id=UUID(system_id),
                client=self._get_api_client(),
                interval=interval,
                resolution=res_enum,
            )
            if response.status_code.value != 200:
                self.logger.warning(f"Status Code {response.status_code.value} for system {system_id}")
                return None
            return json.loads(response.content)
        except Exception as e:
            self.logger.error(e)
            return None

    def retrieve_historical_data(
        self, start: str, end: str, resolution: str = "15m"
    ) -> list[dict[str, Any]]:
        """Fetch historical data for all discovered systems.

        Systems that return an error are skipped; see
        :meth:`retrieve_historical_data_by_id` for parameter details.
        """
        results: list[dict[str, Any]] = []
        for system_id in self.gateways:
            try:
                data = self.retrieve_historical_data_by_id(system_id, start, end, resolution)
                if data is not None:
                    results.append(data)
            except Exception as e:
                self.logger.error(e)
        return results
