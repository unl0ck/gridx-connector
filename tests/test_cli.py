"""Tests for the CLI entry point."""

import json
import sys

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
        mocker.patch("gridx_connector.cli.retrieve_live_data", return_value=[])
        main()  # must not raise

    def test_rejects_viessmann_oem(self, monkeypatch, mocker):
        """viessmann is no longer a valid OEM (realm shut down; config removed)."""
        monkeypatch.setattr(sys, "argv", ["gridx", "-u", "u", "-p", "p", "-o", "viessmann"])
        with pytest.raises(SystemExit) as exc:
            main()
        assert exc.value.code != 0


class TestRetrieveLiveData:
    def test_default_oem_is_eon_home(self, mocker):
        mock_connector = mocker.MagicMock()
        mock_connector.retrieve_live_data.return_value = [{"consumption": 100}]
        mocker.patch("gridx_connector.cli.GridboxConnector", return_value=mock_connector)
        mocker.patch(
            "gridx_connector.cli.files",
            return_value=mocker.MagicMock(
                joinpath=lambda *args: mocker.MagicMock(
                    __enter__=lambda s: s,
                    __exit__=lambda s, *a: None,
                    read=lambda: json.dumps(
                        {
                            "urls": {
                                "login": "https://example.com",
                                "gateways": "https://example.com",
                                "live": "https://example.com/{}",
                                "historical": "https://example.com/{}/{}{}",
                            },
                            "login": {
                                "grant_type": "password",
                                "username": "",
                                "password": "",
                                "audience": "x",
                                "client_id": "x",
                                "scope": "x",
                                "realm": "x",
                                "client_secret": "",
                            },
                        }
                    ),
                )
            ),
        )
        import inspect

        sig = inspect.signature(retrieve_live_data)
        default_oem = sig.parameters["oem"].default
        assert default_oem == "eon-home"

    def test_main_passes_args_to_retrieve(self, monkeypatch, mocker):
        monkeypatch.setattr(sys, "argv", ["gridx", "-u", "testuser", "-p", "testpass"])
        mock_retrieve = mocker.patch("gridx_connector.cli.retrieve_live_data", return_value=[])
        main()
        mock_retrieve.assert_called_once_with("testuser", "testpass", "eon-home")

    def test_viessmann_emits_deprecation_warning(self, mocker, tmp_path):
        """retrieve_live_data warns when oem='viessmann'."""
        import warnings

        config_data = {
            "urls": {
                "login": "https://example.com/token",
                "gateways": "https://example.com/gateways",
                "live": "https://example.com/systems/{}/live",
                "historical": "https://example.com/systems/{}/historical?interval={}&resolution={}",
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
