"""Tests for AsyncGridboxConnector."""

import json
import time
from http import HTTPStatus

import pytest

from gridx_connector.async_connector import AsyncGridboxConnector
from gridx_connector_api import AuthenticatedClient
from tests.conftest import MOCK_HISTORICAL_DATA, MOCK_LIVE_DATA, MOCK_SYSTEM_IDS


def _mock_token_response(mocker):
    response = mocker.Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {
        "id_token": "async-token",
        "expires_in": 3600,
        "expires_at": time.time() + 3600,
    }
    return response


def _mock_api_response(mocker, payload, status: int = 200):
    response = mocker.Mock()
    response.status_code = HTTPStatus(status)
    response.content = json.dumps(payload).encode()
    return response


@pytest.mark.asyncio
async def test_initialize_populates_gateways(eon_home_config, mocker):
    connector = AsyncGridboxConnector(eon_home_config)

    httpx_client = mocker.AsyncMock()
    httpx_client.post.return_value = _mock_token_response(mocker)
    async_ctx = mocker.AsyncMock()
    async_ctx.__aenter__.return_value = httpx_client
    async_ctx.__aexit__.return_value = None
    mocker.patch("gridx_connector.async_connector.httpx.AsyncClient", return_value=async_ctx)

    systems_response = _mock_api_response(mocker, [{"id": system_id} for system_id in MOCK_SYSTEM_IDS])
    mocker.patch(
        "gridx_connector.async_connector._get_systems_async",
        new=mocker.AsyncMock(return_value=systems_response),
    )

    await connector.initialize()

    assert connector.get_gateways() == MOCK_SYSTEM_IDS


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("status", "expected"),
    [(401, PermissionError), (403, PermissionError), (500, RuntimeError)],
)
async def test_get_gateway_id_raises_on_error_status(eon_home_config, mocker, status, expected):
    connector = AsyncGridboxConnector(eon_home_config)

    systems_response = _mock_api_response(mocker, {}, status=status)
    mocker.patch(
        "gridx_connector.async_connector._get_systems_async",
        new=mocker.AsyncMock(return_value=systems_response),
    )
    mocker.patch.object(connector, "_get_api_client", new=mocker.AsyncMock(return_value=mocker.Mock()))

    with pytest.raises(expected):
        await connector.get_gateway_id()


@pytest.mark.asyncio
async def test_ensure_valid_token_refreshes_when_expired(eon_home_config, mocker):
    connector = AsyncGridboxConnector(eon_home_config)
    connector.token = {"expires_at": time.time() - 1}
    connector._api_client = mocker.Mock(spec=AuthenticatedClient)

    refresh_mock = mocker.patch.object(connector, "get_new_token", new=mocker.AsyncMock())

    await connector.ensure_valid_token()

    refresh_mock.assert_awaited_once()


@pytest.mark.asyncio
async def test_initialize_is_idempotent_and_fetches_token_once(eon_home_config, mocker):
    connector = AsyncGridboxConnector(eon_home_config)

    token_mock = mocker.patch.object(connector, "get_new_token", new=mocker.AsyncMock())
    gateway_mock = mocker.patch.object(connector, "get_gateway_id", new=mocker.AsyncMock())

    await connector.initialize()
    await connector.initialize()

    token_mock.assert_awaited_once()
    gateway_mock.assert_awaited_once()


@pytest.mark.asyncio
async def test_retrieve_live_data_returns_all_non_null_results(eon_home_config, mocker):
    connector = AsyncGridboxConnector(eon_home_config)
    connector.gateways = MOCK_SYSTEM_IDS.copy()

    data_by_id = {
        MOCK_SYSTEM_IDS[0]: {"consumption": 1},
        MOCK_SYSTEM_IDS[1]: {"consumption": 2},
    }

    async def _fake_live(system_id: str):
        return data_by_id[system_id]

    mocker.patch.object(connector, "retrieve_live_data_by_id", side_effect=_fake_live)

    result = await connector.retrieve_live_data()

    assert result == [{"consumption": 1}, {"consumption": 2}]


@pytest.mark.asyncio
async def test_retrieve_live_data_by_id_returns_none_on_non_200(eon_home_config, mocker):
    connector = AsyncGridboxConnector(eon_home_config)

    api_response = _mock_api_response(mocker, MOCK_LIVE_DATA, status=500)
    mocker.patch("gridx_connector.async_connector._get_live_async", new=mocker.AsyncMock(return_value=api_response))
    mocker.patch.object(connector, "_get_api_client", new=mocker.AsyncMock(return_value=mocker.Mock()))

    result = await connector.retrieve_live_data_by_id(MOCK_SYSTEM_IDS[0])

    assert result is None


@pytest.mark.asyncio
@pytest.mark.parametrize("status", [401, 403])
async def test_retrieve_live_data_by_id_raises_on_auth_status(eon_home_config, mocker, status):
    connector = AsyncGridboxConnector(eon_home_config)

    api_response = _mock_api_response(mocker, {}, status=status)
    mocker.patch("gridx_connector.async_connector._get_live_async", new=mocker.AsyncMock(return_value=api_response))
    mocker.patch.object(connector, "_get_api_client", new=mocker.AsyncMock(return_value=mocker.Mock()))

    with pytest.raises(PermissionError):
        await connector.retrieve_live_data_by_id(MOCK_SYSTEM_IDS[0])


@pytest.mark.asyncio
async def test_retrieve_live_data_propagates_auth_error(eon_home_config, mocker):
    connector = AsyncGridboxConnector(eon_home_config)
    connector.gateways = MOCK_SYSTEM_IDS.copy()

    mocker.patch.object(
        connector,
        "retrieve_live_data_by_id",
        side_effect=PermissionError("expired credentials"),
    )

    with pytest.raises(PermissionError):
        await connector.retrieve_live_data()


@pytest.mark.asyncio
async def test_retrieve_live_data_tolerates_partial_failure(eon_home_config, mocker):
    connector = AsyncGridboxConnector(eon_home_config)
    connector.gateways = MOCK_SYSTEM_IDS.copy()

    results = {
        MOCK_SYSTEM_IDS[0]: {"consumption": 1},
        MOCK_SYSTEM_IDS[1]: RuntimeError("boom"),
    }

    async def _fake_live(system_id: str):
        result = results[system_id]
        if isinstance(result, Exception):
            raise result
        return result

    mocker.patch.object(connector, "retrieve_live_data_by_id", side_effect=_fake_live)

    result = await connector.retrieve_live_data()

    assert result == [{"consumption": 1}]


@pytest.mark.asyncio
async def test_retrieve_live_data_raises_when_all_systems_fail(eon_home_config, mocker):
    connector = AsyncGridboxConnector(eon_home_config)
    connector.gateways = MOCK_SYSTEM_IDS.copy()

    mocker.patch.object(
        connector,
        "retrieve_live_data_by_id",
        side_effect=RuntimeError("boom"),
    )

    with pytest.raises(RuntimeError):
        await connector.retrieve_live_data()


def test_constructor_does_not_attach_log_handlers(eon_home_config):
    connector = AsyncGridboxConnector(eon_home_config)

    assert connector.logger.handlers == []


def test_env_vars_override_credentials(eon_home_config, monkeypatch):
    monkeypatch.setenv("GRIDX_USERNAME", "env-user")
    monkeypatch.setenv("GRIDX_PASSWORD", "env-pass")

    connector = AsyncGridboxConnector(eon_home_config)

    assert connector.username == "env-user"
    assert connector.password == "env-pass"


def test_generic_os_env_vars_are_ignored(eon_home_config, monkeypatch):
    monkeypatch.setenv("USERNAME", "os-user")
    monkeypatch.setenv("PASSWORD", "os-pass")

    connector = AsyncGridboxConnector(eon_home_config)

    assert connector.username == eon_home_config["login"]["username"]
    assert connector.password == eon_home_config["login"]["password"]


@pytest.mark.asyncio
async def test_retrieve_historical_data_by_id_invalid_resolution_falls_back(eon_home_config, mocker):
    connector = AsyncGridboxConnector(eon_home_config)

    api_response = _mock_api_response(mocker, MOCK_HISTORICAL_DATA)
    historical_mock = mocker.patch(
        "gridx_connector.async_connector._get_historical_async",
        new=mocker.AsyncMock(return_value=api_response),
    )
    mocker.patch.object(connector, "_get_api_client", new=mocker.AsyncMock(return_value=mocker.Mock()))

    result = await connector.retrieve_historical_data_by_id(
        system_id=MOCK_SYSTEM_IDS[0],
        start="2023-01-01T00:00:00Z",
        end="2023-01-02T00:00:00Z",
        resolution="invalid",
    )

    assert result == MOCK_HISTORICAL_DATA
    assert historical_mock.await_count == 1


@pytest.mark.asyncio
async def test_get_new_token_uses_injected_httpx_client(eon_home_config, mocker):
    injected_client = mocker.AsyncMock()
    injected_client.post.return_value = _mock_token_response(mocker)

    connector = AsyncGridboxConnector(
        eon_home_config,
        httpx_client=injected_client,
        owns_httpx_client=False,
    )

    await connector.get_new_token()

    injected_client.post.assert_awaited_once()
    assert connector._api_client is not None


@pytest.mark.asyncio
async def test_close_closes_only_owned_injected_client(eon_home_config, mocker):
    injected_client = mocker.AsyncMock()
    connector = AsyncGridboxConnector(
        eon_home_config,
        httpx_client=injected_client,
        owns_httpx_client=True,
    )

    await connector.close()

    injected_client.aclose.assert_awaited_once()


@pytest.mark.asyncio
async def test_close_does_not_close_unowned_injected_client(eon_home_config, mocker):
    injected_client = mocker.AsyncMock()
    connector = AsyncGridboxConnector(
        eon_home_config,
        httpx_client=injected_client,
        owns_httpx_client=False,
    )

    await connector.close()

    injected_client.aclose.assert_not_awaited()
