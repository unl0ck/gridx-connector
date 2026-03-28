"""Tests for GridboxConnector."""

import time
from http import HTTPStatus

from tests.conftest import (
    MOCK_HISTORICAL_DATA,
    MOCK_LIVE_DATA,
    MOCK_SYSTEM_IDS,
    MOCK_TOKEN,
    _make_mock_response,
)


class TestInit:
    def test_config_is_stored(self, connector, eon_home_config):
        assert connector.config == eon_home_config

    def test_login_url_is_extracted(self, connector, eon_home_config):
        assert connector.login_url == eon_home_config["urls"]["login"]

    def test_gateways_populated_on_init(self, connector):
        assert connector.get_gateways() == MOCK_SYSTEM_IDS

    def test_gateways_are_instance_level(self, eon_home_config, mocker, mock_api):
        """Two connectors must not share the same gateways list."""
        mocker.patch(
            "authlib.integrations.requests_client.OAuth2Session.fetch_token",
            return_value=MOCK_TOKEN,
        )
        from gridx_connector import GridboxConnector

        c1 = GridboxConnector(eon_home_config)
        c2 = GridboxConnector(eon_home_config)
        assert c1.gateways is not c2.gateways


class TestTokenHandling:
    def test_ensure_valid_token_skips_when_fresh(self, connector, mocker):
        connector.token["expires_at"] = time.time() + 3600
        spy = mocker.patch.object(connector, "get_new_token")
        connector.ensure_valid_token()
        spy.assert_not_called()

    def test_ensure_valid_token_refreshes_when_expired(self, connector, mocker):
        connector.token["expires_at"] = time.time() - 1
        spy = mocker.patch.object(connector, "get_new_token")
        connector.ensure_valid_token()
        spy.assert_called_once()

    def test_api_client_is_created_after_init(self, connector):
        from gridx_connector_api import AuthenticatedClient

        assert isinstance(connector._api_client, AuthenticatedClient)


class TestLiveData:
    def test_retrieve_live_data_returns_list(self, connector):
        result = connector.retrieve_live_data()
        assert isinstance(result, list)
        assert len(result) == len(MOCK_SYSTEM_IDS)

    def test_retrieve_live_data_contains_expected_fields(self, connector):
        result = connector.retrieve_live_data()
        first = result[0]
        assert first["consumption"] == MOCK_LIVE_DATA["consumption"]
        assert first["photovoltaic"] == MOCK_LIVE_DATA["photovoltaic"]
        assert "selfSufficiencyRate" in first

    def test_retrieve_live_data_by_id_returns_dict(self, connector):
        result = connector.retrieve_live_data_by_id("11111111-1111-1111-1111-111111111111")
        assert result == MOCK_LIVE_DATA

    def test_retrieve_live_data_by_id_logs_on_error_status(self, connector, mocker, caplog):
        mock_response = mocker.Mock()
        mock_response.status_code = HTTPStatus(403)
        mocker.patch("gridx_connector.GridboxConnector._get_live", return_value=mock_response)
        import logging

        with caplog.at_level(logging.WARNING):
            result = connector.retrieve_live_data_by_id("11111111-1111-1111-1111-111111111111")
        assert result is None
        assert "403" in caplog.text

    def test_retrieve_live_data_by_id_returns_none_on_exception(self, connector, mocker):
        mocker.patch("gridx_connector.GridboxConnector._get_live", side_effect=RuntimeError("network error"))
        result = connector.retrieve_live_data_by_id("11111111-1111-1111-1111-111111111111")
        assert result is None


class TestHistoricalData:
    def test_retrieve_historical_data_returns_list(self, connector):
        result = connector.retrieve_historical_data(
            start="2023-01-01T00:00:00+01:00",
            end="2023-01-02T00:00:00+01:00",
        )
        assert isinstance(result, list)
        assert len(result) == len(MOCK_SYSTEM_IDS)

    def test_retrieve_historical_data_default_resolution(self, connector, mocker):
        from gridx_connector_api.models.get_systems_system_id_historical_resolution import (
            GetSystemsSystemIDHistoricalResolution,
        )

        mock_patch = mocker.patch(
            "gridx_connector.GridboxConnector._get_historical",
            return_value=_make_mock_response(mocker, MOCK_HISTORICAL_DATA),
        )
        connector.retrieve_historical_data(start="2023-01-01T00:00:00Z", end="2023-01-02T00:00:00Z")
        for call in mock_patch.call_args_list:
            assert call.kwargs["resolution"] == GetSystemsSystemIDHistoricalResolution.VALUE_0  # "15m"

    def test_retrieve_historical_data_custom_resolution(self, connector, mocker):
        from gridx_connector_api.models.get_systems_system_id_historical_resolution import (
            GetSystemsSystemIDHistoricalResolution,
        )

        mock_patch = mocker.patch(
            "gridx_connector.GridboxConnector._get_historical",
            return_value=_make_mock_response(mocker, MOCK_HISTORICAL_DATA),
        )
        connector.retrieve_historical_data(
            start="2023-01-01T00:00:00Z",
            end="2023-01-02T00:00:00Z",
            resolution="1h",
        )
        for call in mock_patch.call_args_list:
            assert call.kwargs["resolution"] == GetSystemsSystemIDHistoricalResolution.VALUE_1  # "1h"

    def test_retrieve_historical_data_invalid_resolution_uses_default(self, connector, mocker):
        from gridx_connector_api.models.get_systems_system_id_historical_resolution import (
            GetSystemsSystemIDHistoricalResolution,
        )

        mock_patch = mocker.patch(
            "gridx_connector.GridboxConnector._get_historical",
            return_value=_make_mock_response(mocker, MOCK_HISTORICAL_DATA),
        )
        connector.retrieve_historical_data(
            start="2023-01-01T00:00:00Z",
            end="2023-01-02T00:00:00Z",
            resolution="invalid",
        )
        for call in mock_patch.call_args_list:
            assert call.kwargs["resolution"] == GetSystemsSystemIDHistoricalResolution.VALUE_0  # fallback "15m"
