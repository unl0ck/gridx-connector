import time
from unittest.mock import MagicMock, patch, call

import pytest

from gridx_connector.GridboxConnector import GridboxConnector


def _make_config():
    """Return a minimal valid config dict."""
    return {
        "urls": {
            "login": "https://example.com/oauth/token",
            "gateways": "https://example.com/gateways",
            "live": "https://example.com/systems/{}/live",
            "historical": "https://example.com/systems/{}/historical?interval={}&resolution={}",
        },
        "login": {
            "grant_type": "password",
            "username": "user",
            "password": "pass",
            "audience": "my.gridx",
            "client_id": "test-client-id",
            "client_secret": "",
            "scope": "openid email",
            "realm": "test-realm",
        },
    }


def _create_connector(gateways=None):
    """Create a GridboxConnector bypassing __init__ side effects (auth + gateway fetch)."""
    config = _make_config()
    with patch.object(GridboxConnector, "__init__", lambda self, *a, **kw: None):
        connector = GridboxConnector.__new__(GridboxConnector)
    connector.config = config
    connector.login_url = config["urls"]["login"]
    connector.login_body = config["login"]
    connector.gateway_url = config["urls"]["gateways"]
    connector.live_url = config["urls"]["live"]
    connector.historical_url = config["urls"]["historical"]
    connector.gateways = gateways or []
    connector.token = {"id_token": "fake-token", "expires_at": time.time() + 3600}
    connector.client = MagicMock()
    connector.logger = MagicMock()
    return connector


# --- __init__ and init_auth ---

class TestInit:
    @patch.object(GridboxConnector, "init_auth")
    def test_init_sets_urls_from_config(self, mock_auth):
        config = _make_config()
        connector = GridboxConnector(config)
        assert connector.login_url == config["urls"]["login"]
        assert connector.gateway_url == config["urls"]["gateways"]
        assert connector.live_url == config["urls"]["live"]
        assert connector.historical_url == config["urls"]["historical"]

    @patch.object(GridboxConnector, "init_auth")
    def test_init_calls_init_auth(self, mock_auth):
        config = _make_config()
        connector = GridboxConnector(config)
        mock_auth.assert_called_once()

    @patch.object(GridboxConnector, "init_auth")
    def test_init_reads_env_username(self, mock_auth):
        config = _make_config()
        with patch.dict("os.environ", {"USERNAME": "env-user", "PASSWORD": "env-pass"}):
            connector = GridboxConnector(config)
        assert connector.username == "env-user"
        assert connector.password == "env-pass"


# --- Token management ---

class TestTokenManagement:
    def test_ensure_valid_token_does_nothing_when_valid(self):
        connector = _create_connector()
        connector.token = {"expires_at": time.time() + 3600, "id_token": "valid"}
        with patch.object(connector, "get_new_token") as mock:
            connector.ensure_valid_token()
            mock.assert_not_called()

    def test_ensure_valid_token_refreshes_when_expired(self):
        connector = _create_connector()
        connector.token = {"expires_at": time.time() - 10, "id_token": "expired"}
        with patch.object(connector, "get_new_token") as mock:
            connector.ensure_valid_token()
            mock.assert_called_once()

    def test_ensure_valid_token_refreshes_when_no_expiry(self):
        connector = _create_connector()
        connector.token = {"id_token": "no-expiry"}
        with patch.object(connector, "get_new_token") as mock:
            connector.ensure_valid_token()
            mock.assert_called_once()

    def test_get_header_returns_bearer_token(self):
        connector = _create_connector()
        header = connector.get_header()
        assert header == {"Authorization": "Bearer fake-token"}

    def test_get_header_checks_token_validity(self):
        connector = _create_connector()
        with patch.object(connector, "ensure_valid_token") as mock:
            connector.get_header()
            mock.assert_called_once()


# --- Gateway discovery ---

class TestGetGatewayId:
    def test_success(self):
        connector = _create_connector()
        gateway_response = [
            {"system": {"id": "gw-001"}},
            {"system": {"id": "gw-002"}},
        ]
        mock_response = MagicMock()
        mock_response.json.return_value = gateway_response

        with patch("gridx_connector.GridboxConnector.requests.get", return_value=mock_response):
            connector.get_gateway_id()

        assert connector.gateways == ["gw-001", "gw-002"]

    def test_clears_existing_gateways(self):
        connector = _create_connector(gateways=["old-gw"])
        mock_response = MagicMock()
        mock_response.json.return_value = [{"system": {"id": "new-gw"}}]

        with patch("gridx_connector.GridboxConnector.requests.get", return_value=mock_response):
            connector.get_gateway_id()

        assert connector.gateways == ["new-gw"]

    def test_empty_gateway_list(self):
        connector = _create_connector()
        mock_response = MagicMock()
        mock_response.json.return_value = []

        with patch("gridx_connector.GridboxConnector.requests.get", return_value=mock_response):
            connector.get_gateway_id()

        assert connector.gateways == []

    def test_get_gateways_returns_list(self):
        connector = _create_connector(gateways=["gw-1", "gw-2"])
        assert connector.get_gateways() == ["gw-1", "gw-2"]


# --- Live data ---

class TestRetrieveLiveData:
    def test_by_id_success(self):
        connector = _create_connector()
        live_json = {"consumption": 500, "photovoltaic": 400}
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = live_json

        with patch("gridx_connector.GridboxConnector.requests.get", return_value=mock_response):
            result = connector.retrieve_live_data_by_id("sys-001")

        assert result.status_code == 200
        assert result.json() == live_json

    def test_by_id_non_200_returns_response(self):
        connector = _create_connector()
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.json.return_value = {"error": "forbidden"}

        with patch("gridx_connector.GridboxConnector.requests.get", return_value=mock_response):
            result = connector.retrieve_live_data_by_id("sys-001")

        assert result.status_code == 403
        connector.logger.warning.assert_called_once()

    def test_by_id_exception_returns_none(self):
        connector = _create_connector()

        with patch("gridx_connector.GridboxConnector.requests.get", side_effect=ConnectionError("down")):
            result = connector.retrieve_live_data_by_id("sys-001")

        assert result is None
        connector.logger.error.assert_called_once()

    def test_retrieve_multiple_gateways(self):
        connector = _create_connector(gateways=["gw-1", "gw-2"])
        live_json_1 = {"consumption": 100}
        live_json_2 = {"consumption": 200}

        resp1 = MagicMock(status_code=200)
        resp1.json.return_value = live_json_1
        resp2 = MagicMock(status_code=200)
        resp2.json.return_value = live_json_2

        with patch("gridx_connector.GridboxConnector.requests.get", side_effect=[resp1, resp2]):
            results = connector.retrieve_live_data()

        assert len(results) == 2
        assert results[0] == live_json_1
        assert results[1] == live_json_2

    def test_retrieve_skips_failed_gateways(self):
        connector = _create_connector(gateways=["gw-ok", "gw-fail"])
        resp_ok = MagicMock(status_code=200)
        resp_ok.json.return_value = {"consumption": 100}
        resp_fail = MagicMock(status_code=500)
        resp_fail.json.return_value = {"error": "internal"}

        with patch("gridx_connector.GridboxConnector.requests.get", side_effect=[resp_ok, resp_fail]):
            results = connector.retrieve_live_data()

        assert len(results) == 1

    def test_retrieve_empty_gateways(self):
        connector = _create_connector(gateways=[])
        results = connector.retrieve_live_data()
        assert results == []


# --- Historical data ---

class TestRetrieveHistoricalData:
    def test_by_id_success(self):
        connector = _create_connector()
        hist_json = [{"measuredAt": "2023-08-04T00:00:00Z", "consumption": 1000}]
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = hist_json

        with patch("gridx_connector.GridboxConnector.requests.get", return_value=mock_response):
            result = connector.retrieve_historical_data_by_id(
                "sys-001", "2023-08-04T00:00:00Z", "2023-08-05T00:00:00Z"
            )

        assert result.status_code == 200
        assert result.json() == hist_json

    def test_by_id_custom_resolution(self):
        connector = _create_connector()
        mock_response = MagicMock(status_code=200)
        mock_response.json.return_value = []

        with patch("gridx_connector.GridboxConnector.requests.get", return_value=mock_response) as mock_get:
            connector.retrieve_historical_data_by_id(
                "sys-001", "2023-08-04T00:00:00Z", "2023-08-05T00:00:00Z", resolution="1h"
            )

        called_url = mock_get.call_args[0][0]
        assert "resolution=1h" in called_url

    def test_by_id_non_200_returns_response(self):
        connector = _create_connector()
        mock_response = MagicMock(status_code=404)
        mock_response.json.return_value = {"error": "not found"}

        with patch("gridx_connector.GridboxConnector.requests.get", return_value=mock_response):
            result = connector.retrieve_historical_data_by_id(
                "sys-001", "2023-08-04T00:00:00Z", "2023-08-05T00:00:00Z"
            )

        assert result.status_code == 404
        assert connector.logger.warning.call_count >= 1

    def test_by_id_exception_returns_none(self):
        connector = _create_connector()

        with patch("gridx_connector.GridboxConnector.requests.get", side_effect=ConnectionError("down")):
            result = connector.retrieve_historical_data_by_id(
                "sys-001", "2023-08-04T00:00:00Z", "2023-08-05T00:00:00Z"
            )

        assert result is None
        connector.logger.error.assert_called_once()

    def test_retrieve_multiple_gateways(self):
        connector = _create_connector(gateways=["gw-1", "gw-2"])
        hist1 = [{"consumption": 100}]
        hist2 = [{"consumption": 200}]

        resp1 = MagicMock(status_code=200)
        resp1.json.return_value = hist1
        resp2 = MagicMock(status_code=200)
        resp2.json.return_value = hist2

        with patch("gridx_connector.GridboxConnector.requests.get", side_effect=[resp1, resp2]):
            results = connector.retrieve_historical_data(
                "2023-08-04T00:00:00Z", "2023-08-05T00:00:00Z"
            )

        assert len(results) == 2

    def test_retrieve_empty_gateways(self):
        connector = _create_connector(gateways=[])
        results = connector.retrieve_historical_data(
            "2023-08-04T00:00:00Z", "2023-08-05T00:00:00Z"
        )
        assert results == []

    def test_url_encodes_interval(self):
        connector = _create_connector()
        mock_response = MagicMock(status_code=200)
        mock_response.json.return_value = []

        with patch("gridx_connector.GridboxConnector.requests.get", return_value=mock_response) as mock_get:
            connector.retrieve_historical_data_by_id(
                "sys-001", "2023-08-04T00:00:00Z", "2023-08-05T00:00:00Z"
            )

        called_url = mock_get.call_args[0][0]
        # Colons in timestamps should be URL-encoded as %3A
        assert "%3A" in called_url
        assert "2023-08-04" in called_url
        assert "2023-08-05" in called_url


# --- Logging ---

class TestLogging:
    @patch.object(GridboxConnector, "init_auth")
    def test_init_creates_logger_when_none_passed(self, mock_auth):
        config = _make_config()
        connector = GridboxConnector(config)
        assert connector.logger is not None

    def test_set_loglevel(self):
        connector = _create_connector()
        connector.logger = MagicMock()
        connector.set_loglevel("DEBUG")
        connector.logger.setLevel.assert_called_once()


# --- Supported OEM ---

class TestSupportedOEM:
    def test_constants(self):
        from gridx_connector.supported_oem import SupportedOEM
        assert SupportedOEM.VIESSMANN == "viessmann"
        assert SupportedOEM.EON_HOME == "eon-home"
