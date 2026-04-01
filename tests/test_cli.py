"""Tests for the CLI entry point."""

import inspect
import json
import sys
import warnings

import pytest

from gridx_connector.cli import main, retrieve_live_data


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
            "urls": {
                "login": "https://example.com/token",
            },
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
