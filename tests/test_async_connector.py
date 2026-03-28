"""Tests for AsyncGridboxConnector."""

import json
import time
from http import HTTPStatus

import pytest

from gridx_connector.async_connector import AsyncGridboxConnector
from tests.conftest import MOCK_HISTORICAL_DATA, MOCK_LIVE_DATA, MOCK_SYSTEM_IDS


class _MockSystem:
    def __init__(self, system_id: str) -> None:
        self.additional_properties = {"id": system_id}


def _mock_token_response(mocker):
    response = mocker.Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {
        "id_token": "async-token",
        "expires_in": 3600,
        "expires_at": time.time() + 3600,
    }
    return response


def _mock_api_response(mocker, payload: dict, status: int = 200):
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

    systems = [_MockSystem(system_id) for system_id in MOCK_SYSTEM_IDS]
    mocker.patch("gridx_connector.async_connector._get_systems_async", new=mocker.AsyncMock(return_value=systems))

    await connector.initialize()

    assert connector.get_gateways() == MOCK_SYSTEM_IDS


@pytest.mark.asyncio
async def test_ensure_valid_token_refreshes_when_expired(eon_home_config, mocker):
    connector = AsyncGridboxConnector(eon_home_config)
    connector.token = {"expires_at": time.time() - 1}
    connector._api_client = object()

    refresh_mock = mocker.patch.object(connector, "get_new_token", new=mocker.AsyncMock())

    await connector.ensure_valid_token()

    refresh_mock.assert_awaited_once()


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

    api_response = _mock_api_response(mocker, MOCK_LIVE_DATA, status=403)
    mocker.patch("gridx_connector.async_connector._get_live_async", new=mocker.AsyncMock(return_value=api_response))
    mocker.patch.object(connector, "_get_api_client", new=mocker.AsyncMock(return_value=mocker.Mock()))

    result = await connector.retrieve_live_data_by_id(MOCK_SYSTEM_IDS[0])

    assert result is None


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
