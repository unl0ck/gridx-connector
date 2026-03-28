"""Shared pytest fixtures for gridx-connector tests."""

import json
import time
from http import HTTPStatus

import pytest

MOCK_TOKEN = {
    "access_token": "mock-access-token",
    "id_token": "mock-id-token",
    "token_type": "Bearer",
    "expires_at": time.time() + 3600,
    "expires_in": 3600,
}

MOCK_LIVE_DATA = {
    "consumption": 496,
    "directConsumption": 413,
    "directConsumptionEV": 0,
    "directConsumptionHeatPump": 0,
    "directConsumptionHeater": 0,
    "directConsumptionHousehold": 413,
    "directConsumptionRate": 1,
    "grid": 83,
    "measuredAt": "2023-08-04T11:29:43Z",
    "photovoltaic": 413,
    "production": 413,
    "selfConsumption": 413,
    "selfConsumptionRate": 1.0,
    "selfSufficiencyRate": 0.8326612903225806,
    "selfSupply": 413,
    "totalConsumption": 496,
}

MOCK_HISTORICAL_DATA = {
    "measurements": [MOCK_LIVE_DATA],
    "total": MOCK_LIVE_DATA,
}

MOCK_SYSTEM_IDS = [
    "11111111-1111-1111-1111-111111111111",
    "22222222-2222-2222-2222-222222222222",
]


def _make_mock_system(mocker, system_id: str):
    s = mocker.Mock()
    s.additional_properties = {"id": system_id}
    return s


def _make_mock_response(mocker, data: dict, status: int = 200):
    resp = mocker.Mock()
    resp.status_code = HTTPStatus(status)
    resp.content = json.dumps(data).encode()
    return resp


@pytest.fixture
def eon_home_config():
    """Minimal eon-home config. API URLs (gateways/live/historical) are handled by gridx_connector_api."""
    return {
        "urls": {
            "login": "https://gridx.eu.auth0.com/oauth/token",
        },
        "login": {
            "grant_type": "http://auth0.com/oauth/grant-type/password-realm",
            "username": "test@example.com",
            "password": "testpassword",
            "audience": "my.gridx",
            "client_id": "test-client-id",
            "scope": "email openid offline_access",
            "realm": "eon-home-authentication-db",
            "client_secret": "",
        },
    }


@pytest.fixture
def mock_api(mocker):
    """Patch all gridx_connector_api functions used by GridboxConnector."""
    systems = [_make_mock_system(mocker, sid) for sid in MOCK_SYSTEM_IDS]
    mocker.patch("gridx_connector.GridboxConnector._get_systems", return_value=systems)
    mocker.patch(
        "gridx_connector.GridboxConnector._get_live",
        return_value=_make_mock_response(mocker, MOCK_LIVE_DATA),
    )
    mocker.patch(
        "gridx_connector.GridboxConnector._get_historical",
        return_value=_make_mock_response(mocker, MOCK_HISTORICAL_DATA),
    )


@pytest.fixture
def connector(eon_home_config, mocker, mock_api):
    """A fully initialised GridboxConnector with all HTTP calls mocked."""
    mocker.patch(
        "authlib.integrations.requests_client.OAuth2Session.fetch_token",
        return_value=MOCK_TOKEN,
    )
    from gridx_connector import GridboxConnector

    return GridboxConnector(eon_home_config)
