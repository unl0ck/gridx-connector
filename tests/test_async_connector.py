"""Tests for AsyncGridboxConnector, driven through an httpx.MockTransport."""

from __future__ import annotations

import json
import logging
import time
from collections.abc import Callable

import httpx
import pytest

from gridx_connector import (
    AsyncGridboxConnector,
    GridXAuthenticationError,
    GridXConnectionError,
    GridXError,
    GridXResponseError,
    GridXSystem,
)
from tests.conftest import MOCK_HISTORICAL_DATA, MOCK_LIVE_DATA, MOCK_SYSTEM_IDS

TOKEN_URL = "https://gridx.eu.auth0.com/oauth/token"
SYSTEMS = [
    {
        "id": MOCK_SYSTEM_IDS[0],
        "name": "Home",
        "gateways": [{"manufacturer": "gridX", "model": "gridBox", "serialnumber": "GB-1"}],
    },
    {"id": MOCK_SYSTEM_IDS[1], "name": "Cabin", "gateways": []},
]


def _token(**overrides) -> dict:
    token = {"access_token": "access", "id_token": "ident", "expires_in": 3600, "token_type": "Bearer"}
    token.update(overrides)
    return token


class FakeGridX:
    """Programmable stand-in for Auth0 and the gridX API."""

    def __init__(self) -> None:
        self.token_response: dict | Callable[[httpx.Request], httpx.Response] = _token()
        self.systems: list[dict] | int = SYSTEMS
        self.live: dict[str, dict | int] = {sid: MOCK_LIVE_DATA for sid in MOCK_SYSTEM_IDS}
        self.historical: dict[str, dict | int] = {sid: MOCK_HISTORICAL_DATA for sid in MOCK_SYSTEM_IDS}
        self.rejected_tokens: set[str] = set()
        self.raw_responses: dict[str, httpx.Response] = {}
        self.requests: list[httpx.Request] = []

    def handler(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if str(request.url) == TOKEN_URL:
            if callable(self.token_response):
                return self.token_response(request)
            return httpx.Response(200, json=self.token_response)
        bearer = request.headers.get("Authorization", "").removeprefix("Bearer ")
        if bearer in self.rejected_tokens:
            return httpx.Response(401, json={"error": "unauthorized"})
        path = request.url.path
        if path in self.raw_responses:
            return self.raw_responses[path]
        if path == "/systems":
            return self._respond(self.systems)
        if path.endswith("/live"):
            return self._respond(self.live.get(path.split("/")[2], 404))
        if path.endswith("/historical"):
            return self._respond(self.historical.get(path.split("/")[2], 404))
        return httpx.Response(404)

    @staticmethod
    def _respond(body: dict | list | int) -> httpx.Response:
        if isinstance(body, int):
            return httpx.Response(body, json={"message": "error"})
        return httpx.Response(200, json=body)

    def client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(transport=httpx.MockTransport(self.handler))

    def token_requests(self) -> list[httpx.Request]:
        return [r for r in self.requests if str(r.url) == TOKEN_URL]


@pytest.fixture
def fake() -> FakeGridX:
    return FakeGridX()


@pytest.fixture
async def connector(fake: FakeGridX, eon_home_config) -> AsyncGridboxConnector:
    connector = await AsyncGridboxConnector.create(eon_home_config, httpx_client=fake.client(), owns_httpx_client=True)
    yield connector
    await connector.close()


async def test_create_discovers_systems(connector: AsyncGridboxConnector) -> None:
    assert connector.get_gateways() == MOCK_SYSTEM_IDS
    assert connector.systems[MOCK_SYSTEM_IDS[0]] == GridXSystem(
        id=MOCK_SYSTEM_IDS[0], name="Home", manufacturer="gridX", model="gridBox", serial_number="GB-1"
    )
    assert connector.systems[MOCK_SYSTEM_IDS[1]].serial_number is None


async def test_token_request_carries_credentials_but_no_bearer(fake: FakeGridX, connector) -> None:
    (request,) = fake.token_requests()
    body = dict(httpx.QueryParams(request.content.decode()))
    assert body["username"] == "test@example.com"
    assert body["password"] == "testpassword"
    assert body["audience"] == "https://api.gridx.de"
    assert "Authorization" not in request.headers


async def test_api_requests_send_bearer_per_request_without_mutating_client(fake: FakeGridX, eon_home_config) -> None:
    client = fake.client()
    connector = await AsyncGridboxConnector.create(eon_home_config, httpx_client=client)
    await connector.get_live_data()
    api_requests = [r for r in fake.requests if str(r.url) != TOKEN_URL]
    assert api_requests and all(r.headers["Authorization"] == "Bearer access" for r in api_requests)
    assert "Authorization" not in client.headers


@pytest.mark.parametrize(("status", "expected"), [(401, GridXAuthenticationError), (403, GridXAuthenticationError)])
async def test_token_request_auth_error(fake: FakeGridX, eon_home_config, status, expected) -> None:
    fake.token_response = lambda _: httpx.Response(status, json={"error": "access_denied"})
    with pytest.raises(expected):
        await AsyncGridboxConnector.create(eon_home_config, httpx_client=fake.client())


async def test_token_request_server_error(fake: FakeGridX, eon_home_config) -> None:
    fake.token_response = lambda _: httpx.Response(503, text="down")
    with pytest.raises(GridXResponseError) as excinfo:
        await AsyncGridboxConnector.create(eon_home_config, httpx_client=fake.client())
    assert excinfo.value.status_code == 503


async def test_token_response_without_token_is_an_error(fake: FakeGridX, eon_home_config) -> None:
    fake.token_response = {"expires_in": 3600}
    with pytest.raises(GridXResponseError):
        await AsyncGridboxConnector.create(eon_home_config, httpx_client=fake.client())


async def test_network_error_is_a_connection_error(eon_home_config) -> None:
    def boom(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("no route", request=request)

    client = httpx.AsyncClient(transport=httpx.MockTransport(boom))
    with pytest.raises(GridXConnectionError) as excinfo:
        await AsyncGridboxConnector.create(eon_home_config, httpx_client=client)
    assert isinstance(excinfo.value, ConnectionError)
    assert isinstance(excinfo.value, GridXError)


@pytest.mark.parametrize(("status", "expected"), [(401, GridXAuthenticationError), (500, GridXResponseError)])
async def test_discovery_error_statuses(fake: FakeGridX, eon_home_config, status, expected) -> None:
    fake.systems = status
    with pytest.raises(expected):
        await AsyncGridboxConnector.create(eon_home_config, httpx_client=fake.client())


async def test_exceptions_keep_builtin_compatibility() -> None:
    assert issubclass(GridXAuthenticationError, PermissionError)
    assert issubclass(GridXResponseError, RuntimeError)
    assert issubclass(GridXConnectionError, ConnectionError)


async def test_access_token_rejected_falls_back_to_id_token_once(fake: FakeGridX, eon_home_config) -> None:
    fake.rejected_tokens = {"access"}
    connector = await AsyncGridboxConnector.create(eon_home_config, httpx_client=fake.client())
    await connector.get_live_data()
    bearers = [r.headers.get("Authorization") for r in fake.requests if str(r.url) != TOKEN_URL]
    assert bearers[0] == "Bearer access"
    assert bearers[1:] and all(b == "Bearer ident" for b in bearers[1:])


async def test_both_tokens_rejected_raises_auth_error(fake: FakeGridX, eon_home_config) -> None:
    fake.rejected_tokens = {"access", "ident"}
    with pytest.raises(GridXAuthenticationError):
        await AsyncGridboxConnector.create(eon_home_config, httpx_client=fake.client())


async def test_expired_token_is_refreshed_once(fake: FakeGridX, connector: AsyncGridboxConnector) -> None:
    connector.token["expires_at"] = time.time() - 1
    await connector.get_live_data()
    assert len(fake.token_requests()) == 2


async def test_initialize_is_idempotent(fake: FakeGridX, connector: AsyncGridboxConnector) -> None:
    await connector.initialize()
    assert len(fake.token_requests()) == 1
    await connector.initialize(force=True)
    assert len(fake.token_requests()) == 2


async def test_get_live_data_returns_mapping_per_system(connector: AsyncGridboxConnector) -> None:
    data = await connector.get_live_data()
    assert data == {sid: MOCK_LIVE_DATA for sid in MOCK_SYSTEM_IDS}


async def test_get_live_data_subset(connector: AsyncGridboxConnector) -> None:
    data = await connector.get_live_data([MOCK_SYSTEM_IDS[1]])
    assert list(data) == [MOCK_SYSTEM_IDS[1]]


async def test_get_live_data_fails_on_partial_failure(fake: FakeGridX, connector: AsyncGridboxConnector) -> None:
    fake.live[MOCK_SYSTEM_IDS[1]] = 500
    with pytest.raises(GridXResponseError) as excinfo:
        await connector.get_live_data()
    assert MOCK_SYSTEM_IDS[1] in str(excinfo.value)
    assert excinfo.value.status_code == 500


async def test_get_live_data_prefers_auth_error(fake: FakeGridX, connector: AsyncGridboxConnector) -> None:
    fake.live[MOCK_SYSTEM_IDS[0]] = 500
    fake.live[MOCK_SYSTEM_IDS[1]] = 403
    with pytest.raises(GridXAuthenticationError):
        await connector.get_live_data()


async def test_get_live_data_by_id_malformed_json(fake: FakeGridX, connector: AsyncGridboxConnector) -> None:
    fake.raw_responses[f"/systems/{MOCK_SYSTEM_IDS[0]}/live"] = httpx.Response(200, text="not json")
    with pytest.raises(GridXResponseError):
        await connector.get_live_data_by_id(MOCK_SYSTEM_IDS[0])


async def test_retrieve_live_data_tolerates_partial_failure(
    fake: FakeGridX, connector: AsyncGridboxConnector, caplog: pytest.LogCaptureFixture
) -> None:
    fake.live[MOCK_SYSTEM_IDS[1]] = 500
    with caplog.at_level(logging.WARNING):
        data = await connector.retrieve_live_data()
    assert data == [MOCK_LIVE_DATA]
    assert "Status Code 500" in caplog.text


async def test_retrieve_live_data_raises_when_all_fail(fake: FakeGridX, connector: AsyncGridboxConnector) -> None:
    def boom(request: httpx.Request) -> httpx.Response:
        if str(request.url) == TOKEN_URL:
            return httpx.Response(200, json=_token())
        raise httpx.ReadTimeout("slow", request=request)

    connector._httpx_client = httpx.AsyncClient(transport=httpx.MockTransport(boom))
    with pytest.raises(GridXConnectionError):
        await connector.retrieve_live_data()


async def test_retrieve_live_data_propagates_auth_error(fake: FakeGridX, connector: AsyncGridboxConnector) -> None:
    fake.live[MOCK_SYSTEM_IDS[1]] = 403
    with pytest.raises(GridXAuthenticationError):
        await connector.retrieve_live_data()


async def test_retrieve_live_data_without_systems(fake: FakeGridX, eon_home_config) -> None:
    fake.systems = []
    connector = await AsyncGridboxConnector.create(eon_home_config, httpx_client=fake.client())
    assert await connector.retrieve_live_data() == []
    assert await connector.get_live_data() == {}


async def test_get_historical_data_passes_interval_and_resolution(
    fake: FakeGridX, connector: AsyncGridboxConnector
) -> None:
    data = await connector.get_historical_data("2024-01-01T00:00:00+01:00", "2024-01-02T00:00:00+01:00", "1h")
    assert data == {sid: MOCK_HISTORICAL_DATA for sid in MOCK_SYSTEM_IDS}
    request = next(r for r in fake.requests if r.url.path.endswith("/historical"))
    assert request.url.params["interval"] == "2024-01-01T00:00:00+01:00/2024-01-02T00:00:00+01:00"
    assert request.url.params["resolution"] == "1h"


async def test_retrieve_historical_data_returns_list(connector: AsyncGridboxConnector) -> None:
    data = await connector.retrieve_historical_data("a", "b")
    assert data == [MOCK_HISTORICAL_DATA, MOCK_HISTORICAL_DATA]


def test_config_credentials_win_over_env(eon_home_config, monkeypatch) -> None:
    monkeypatch.setenv("GRIDX_USERNAME", "env-user")
    monkeypatch.setenv("GRIDX_PASSWORD", "env-pass")
    connector = AsyncGridboxConnector(eon_home_config)
    assert connector.username == "test@example.com"
    assert connector.password == "testpassword"


def test_env_fills_missing_credentials(eon_home_config, monkeypatch) -> None:
    monkeypatch.setenv("GRIDX_USERNAME", "env-user")
    monkeypatch.setenv("GRIDX_PASSWORD", "env-pass")
    eon_home_config["login"]["username"] = ""
    del eon_home_config["login"]["password"]
    connector = AsyncGridboxConnector(eon_home_config)
    assert (connector.username, connector.password) == ("env-user", "env-pass")


def test_generic_os_env_vars_are_ignored(eon_home_config, monkeypatch) -> None:
    monkeypatch.setenv("USERNAME", "os-user")
    monkeypatch.setenv("PASSWORD", "os-pass")
    eon_home_config["login"]["username"] = ""
    eon_home_config["login"]["password"] = ""
    connector = AsyncGridboxConnector(eon_home_config)
    assert (connector.username, connector.password) == ("", "")


def test_constructor_does_not_attach_log_handlers(eon_home_config) -> None:
    AsyncGridboxConnector(eon_home_config)
    assert logging.getLogger("gridx_connector.async_connector").handlers == []


async def test_close_closes_owned_client(fake: FakeGridX, eon_home_config) -> None:
    client = fake.client()
    connector = await AsyncGridboxConnector.create(eon_home_config, httpx_client=client, owns_httpx_client=True)
    await connector.close()
    assert client.is_closed


async def test_close_keeps_unowned_client_open(fake: FakeGridX, eon_home_config) -> None:
    client = fake.client()
    connector = await AsyncGridboxConnector.create(eon_home_config, httpx_client=client)
    await connector.close()
    assert not client.is_closed
    await client.aclose()


async def test_self_created_client_is_closed_on_exit(fake: FakeGridX, eon_home_config, monkeypatch) -> None:
    monkeypatch.setattr(httpx.AsyncClient, "__init__", _mock_transport_init(fake))
    async with AsyncGridboxConnector(eon_home_config, timeout=7) as connector:
        client = connector._client
        assert client.timeout == httpx.Timeout(7)
        await connector.get_live_data()
    assert client.is_closed


def _mock_transport_init(fake: FakeGridX):
    original = httpx.AsyncClient.__init__

    def init(self, *args, **kwargs):
        kwargs["transport"] = httpx.MockTransport(fake.handler)
        original(self, *args, **kwargs)

    return init


def test_live_fixture_is_json_serialisable() -> None:
    json.dumps(MOCK_LIVE_DATA)
