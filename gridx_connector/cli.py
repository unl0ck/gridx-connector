from __future__ import annotations

import argparse
import json
import warnings
from importlib.resources import files
from typing import Any

from .GridboxConnector import GridboxConnector
from .supported_oem import SupportedOEM

_ALL_OEMS: list[str] = ["eon-home"]


def retrieve_live_data(username: str, password: str, oem: str = SupportedOEM.EON_HOME) -> list[dict[str, Any]]:
    if oem == "viessmann":
        warnings.warn(
            "The Viessmann realm was shut down at end of 2025. Support for 'viessmann' OEM is deprecated.",
            DeprecationWarning,
            stacklevel=2,
        )
    config_file = files("gridx_connector").joinpath("config", f"{oem}.config.json")
    with open(config_file) as file:
        data: dict[str, Any] = json.load(file)
        data["login"]["username"] = username
        data["login"]["password"] = password
        connector = GridboxConnector(data)
        return connector.retrieve_live_data()


def main() -> None:
    parser = argparse.ArgumentParser(description="Retrieve live data from GridX Gridbox.")
    parser.add_argument("-u", "--username", required=True, help="Login username.")
    parser.add_argument("-p", "--password", required=True, help="Login password.")
    parser.add_argument(
        "-o",
        "--oem",
        default=SupportedOEM.EON_HOME,
        choices=_ALL_OEMS,
        help="OEM configuration to use (default: eon-home).",
    )
    args = parser.parse_args()
    live_data = retrieve_live_data(args.username, args.password, args.oem)
    print(live_data)


if __name__ == "__main__":
    main()
