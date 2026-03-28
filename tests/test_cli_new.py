"""Tests for the CLI entry point with new login-url, config, and save-config features."""

import inspect
import json
import sys
import warnings

import pytest

from gridx_connector.cli import _build_config, main, retrieve_live_data


class TestArgparsing:
    def test_exits_without_username(self, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["gridx"])
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code != 0

    def test_exits_without_password(self, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["gridx", "-u", "user"])
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code != 0

    def test_exits_with_invalid_oem(self, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["gridx", "-u", "u", "-p", "p", "-o", "unknown-oem"])
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code != 0

    def test_accepts_eon_home_oem(self, monkeypatch, mocker):
        monkeypatch.setattr(sys, "argv", ["gridx", "-u", "u", "-p", "p", "-o", "eon-home"])
        mocker.patch("gridx_connector.cli._load_oem_config", return_value={})
        mock_inst = mocker.MagicMock()
        mock_inst.retrieve_live_data.return_value = []
        mocker.patch("gridx_connector.cli.GridboxConnector", return_value=mock_inst)
        main()  # must not raise

    def test_rejects_viessmann_oem(self, monkeypatch):
        """viessmann is no longer a valid OEM (realm shut down; config removed)."""
        monkeypatch.setattr(sys, "argv", ["gridx", "-u", "u", "-p", "p", "-o", "viessmann"])
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code != 0

    def test_login_url_requires_client_id_and_realm(self, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["gridx", "-u", "u", "-p", "p", "--login-url", "https://example.com/token"])
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code != 0

    def test_login_url_without_realm_exits(self, monkeypatch):
        monkeypatch.setattr(
            sys,
            "argv",
            ["gridx", "-u", "u", "-p", "p", "--login-url", "https://example.com/token", "--client-id", "abc"],
        )
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code != 0

    def test_oem_and_login_url_are_mutually_exclusive(self, monkeypatch):
        monkeypatch.setattr(
            sys,
            "argv",
            ["gridx", "-u", "u", "-p", "p", "-o", "eon-home", "--login-url", "https://example.com/token"],
        )
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code != 0


class TestRetrieveLiveData:
    def test_default_oem_is_eon_home(self):
        sig = inspect.signature(retrieve_live_data)
        assert sig.parameters["oem"].default == "eon-home"

    def test_main_passes_username_password_to_config_loader(self, monkeypatch, mocker):
        monkeypatch.setattr(sys, "argv", ["gridx", "-u", "testuser", "-p", "testpass"])
        load_mock = mocker.patch("gridx_connector.cli._load_oem_config", return_value={})
        mock_inst = mocker.MagicMock()
        mock_inst.retrieve_live_data.return_value = []
        mocker.patch("gridx_connector.cli.GridboxConnector", return_value=mock_inst)
        main()
        load_mock.assert_called_once_with("eon-home", "testuser", "testpass")

    def test_viessmann_emits_deprecation_warning(self, mocker, tmp_path):
        """retrieve_live_data warns when oem='viessmann'."""
        config_data = {
            "urls": {"login": "https://example.com/token"},
            "login": {
                "grant_type": "pw",
                "username": "",
                "password": "",
                "audience": "x",
                "client_id": "x",
                "scope": "x",
                "realm": "x",
                "client_secret": "",
            },
        }
        cfg_file = tmp_path / "viessmann.config.json"
        cfg_file.write_text(json.dumps(config_data))

        mock_connector = mocker.MagicMock()
        mock_connector.retrieve_live_data.return_value = []
        mocker.patch("gridx_connector.cli.GridboxConnector", return_value=mock_connector)

        resource_mock = mocker.MagicMock()
        resource_mock.joinpath.return_value = str(cfg_file)
        mocker.patch("gridx_connector.cli.files", return_value=resource_mock)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            retrieve_live_data("u", "p", "viessmann")

        assert any(issubclass(warning.category, DeprecationWarning) for warning in w)


class TestLoginUrl:
    def test_build_config_produces_correct_structure(self):
        config = _build_config(
            username="user@example.com",
            password="secret",
            login_url="https://gridx.eu.auth0.com/oauth/token",
            client_id="abc123",
            realm="my-realm",
        )
        assert config["urls"]["login"] == "https://gridx.eu.auth0.com/oauth/token"
        assert config["login"]["client_id"] == "abc123"
        assert config["login"]["realm"] == "my-realm"
        assert config["login"]["audience"] == "my.gridx"
        assert config["login"]["username"] == "user@example.com"

    def test_build_config_custom_audience(self):
        config = _build_config("u", "p", "https://x.com", "id", "realm", audience="custom.audience")
        assert config["login"]["audience"] == "custom.audience"

    def test_main_uses_login_url(self, monkeypatch, mocker):
        monkeypatch.setattr(
            sys,
            "argv",
            [
                "gridx",
                "-u",
                "u",
                "-p",
                "p",
                "--login-url",
                "https://gridx.eu.auth0.com/oauth/token",
                "--client-id",
                "abc",
                "--realm",
                "my-realm",
            ],
        )
        mock_inst = mocker.MagicMock()
        mock_inst.retrieve_live_data.return_value = []
        ctor = mocker.patch("gridx_connector.cli.GridboxConnector", return_value=mock_inst)
        main()
        config_used = ctor.call_args[0][0]
        assert config_used["urls"]["login"] == "https://gridx.eu.auth0.com/oauth/token"
        assert config_used["login"]["client_id"] == "abc"
        assert config_used["login"]["realm"] == "my-realm"

    def test_main_uses_real_eon_gridx_endpoint(self, monkeypatch, mocker):
        """Test with real eon.gridx.de endpoint."""
        monkeypatch.setattr(
            sys,
            "argv",
            [
                "gridx",
                "-u",
                "testuser",
                "-p",
                "testpass",
                "--login-url",
                "https://eon.gridx.de/oauth/token",
                "--client-id",
                "test-client",
                "--realm",
                "eon-home",
            ],
        )
        mock_inst = mocker.MagicMock()
        mock_inst.retrieve_live_data.return_value = []
        ctor = mocker.patch("gridx_connector.cli.GridboxConnector", return_value=mock_inst)
        main()
        config_used = ctor.call_args[0][0]
        assert config_used["urls"]["login"] == "https://eon.gridx.de/oauth/token"
        assert config_used["login"]["client_id"] == "test-client"
        assert config_used["login"]["realm"] == "eon-home"
        assert config_used["login"]["username"] == "testuser"


class TestConfigFile:
    def test_main_loads_custom_config_file(self, monkeypatch, mocker, tmp_path):
        config_data = {
            "urls": {"login": "https://custom.example.com/token"},
            "login": {
                "grant_type": "pw",
                "username": "",
                "password": "",
                "audience": "x",
                "client_id": "custom-id",
                "scope": "x",
                "realm": "custom-realm",
                "client_secret": "",
            },
        }
        cfg_file = tmp_path / "custom.config.json"
        cfg_file.write_text(json.dumps(config_data))

        monkeypatch.setattr(sys, "argv", ["gridx", "-u", "u", "-p", "p", "--config", str(cfg_file)])
        mock_inst = mocker.MagicMock()
        mock_inst.retrieve_live_data.return_value = []
        ctor = mocker.patch("gridx_connector.cli.GridboxConnector", return_value=mock_inst)
        main()
        config_used = ctor.call_args[0][0]
        assert config_used["login"]["client_id"] == "custom-id"
        assert config_used["login"]["username"] == "u"

    def test_main_exits_on_missing_config_file(self, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["gridx", "-u", "u", "-p", "p", "--config", "/nonexistent/path.json"])
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code != 0


class TestSaveConfig:
    def test_save_config_writes_file_without_credentials(self, monkeypatch, mocker, tmp_path):
        out_file = tmp_path / "saved.config.json"
        monkeypatch.setattr(
            sys,
            "argv",
            [
                "gridx",
                "-u",
                "realuser",
                "-p",
                "realpass",
                "--login-url",
                "https://gridx.eu.auth0.com/oauth/token",
                "--client-id",
                "abc",
                "--realm",
                "my-realm",
                "--save-config",
                str(out_file),
            ],
        )
        mock_inst = mocker.MagicMock()
        mock_inst.retrieve_live_data.return_value = []
        mocker.patch("gridx_connector.cli.GridboxConnector", return_value=mock_inst)
        main()

        assert out_file.exists()
        saved = json.loads(out_file.read_text())
        assert saved["login"]["username"] != "realuser"
        assert saved["login"]["password"] != "realpass"
        assert saved["login"]["client_id"] == "abc"
        assert saved["login"]["realm"] == "my-realm"


class TestAsyncMode:
    def test_main_uses_async_mode_when_flag_is_present(self, monkeypatch, mocker):
        monkeypatch.setattr(
            sys,
            "argv",
            ["gridx", "-u", "u", "-p", "p", "--async"],
        )
        load_mock = mocker.patch("gridx_connector.cli._load_oem_config", return_value={"login": {}})
        async_result = [{"consumption": 123}]

        def _fake_asyncio_run(coro):
            coro.close()
            return async_result

        run_mock = mocker.patch("gridx_connector.cli.asyncio.run", side_effect=_fake_asyncio_run)
        connector_ctor = mocker.patch("gridx_connector.cli.GridboxConnector")

        main()

        load_mock.assert_called_once_with("eon-home", "u", "p")
        run_mock.assert_called_once()
        connector_ctor.assert_not_called()

    def test_main_defaults_to_sync_mode_without_flag(self, monkeypatch, mocker):
        monkeypatch.setattr(
            sys,
            "argv",
            ["gridx", "-u", "u", "-p", "p"],
        )
        mocker.patch("gridx_connector.cli._load_oem_config", return_value={"login": {}})
        mock_inst = mocker.MagicMock()
        mock_inst.retrieve_live_data.return_value = []
        connector_ctor = mocker.patch("gridx_connector.cli.GridboxConnector", return_value=mock_inst)
        run_mock = mocker.patch("gridx_connector.cli.asyncio.run")

        main()

        connector_ctor.assert_called_once()
        run_mock.assert_not_called()
