"""OEM login configurations.

The bundled ``config/<oem>.config.json`` files are the single source of truth
for realm, client id, audience and token endpoint; they are also consumed by
the Home Assistant add-on. They are read once at import time so that
:func:`build_login_config` does no file I/O when called from an event loop.
"""

from __future__ import annotations

import copy
import json
import warnings
from importlib.resources import files
from typing import Any

from .supported_oem import SupportedOEM

#: Base URL of the gridX Solution API. It does not depend on the OEM.
API_BASE_URL = "https://api.gridx.de"

_CONFIG_DIR = files("gridx_connector").joinpath("config")

_OEM_CONFIGS: dict[str, dict[str, Any]] = {
    oem: json.loads(_CONFIG_DIR.joinpath(f"{oem}.config.json").read_text(encoding="utf-8"))
    for oem in (SupportedOEM.EON_HOME, "viessmann")
}

#: Auth0 token endpoint shared by all gridX realms.
LOGIN_URL: str = _OEM_CONFIGS[SupportedOEM.EON_HOME]["urls"]["login"]


def supported_oems() -> tuple[str, ...]:
    """Return the OEM identifiers :func:`build_login_config` accepts."""
    return tuple(_OEM_CONFIGS)


def build_login_config(
    username: str,
    password: str,
    oem: str = SupportedOEM.EON_HOME,
) -> dict[str, Any]:
    """Return the bundled connector config for ``oem`` with the given credentials.

    The result can be passed to :class:`~gridx_connector.AsyncGridboxConnector`
    or :class:`~gridx_connector.GridboxConnector` unchanged.

    Raises:
        ValueError: If ``oem`` is unknown.
    """
    try:
        config = copy.deepcopy(_OEM_CONFIGS[oem])
    except KeyError:
        raise ValueError(f"Unknown OEM {oem!r}; supported: {', '.join(_OEM_CONFIGS)}") from None
    if oem == "viessmann":
        warnings.warn(
            "The Viessmann realm was shut down at end of 2025. Support for 'viessmann' OEM is deprecated.",
            DeprecationWarning,
            stacklevel=2,
        )
    config.pop("$schema", None)
    config.pop("comment", None)
    config["login"]["username"] = username
    config["login"]["password"] = password
    return config
