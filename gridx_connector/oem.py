"""OEM login configurations defined in code.

The bundled ``config/*.config.json`` files remain for the CLI's ``--config``
option and for documentation; library consumers should call
:func:`build_login_config` so that realm, client id and audience live in
exactly one place and no file has to be read at runtime.
"""

from __future__ import annotations

import warnings
from typing import Any

from .supported_oem import SupportedOEM

#: Base URL of the gridX Solution API. It does not depend on the OEM.
API_BASE_URL = "https://api.gridx.de"

#: Auth0 token endpoint shared by all gridX realms.
LOGIN_URL = "https://gridx.eu.auth0.com/oauth/token"

_GRANT_TYPE = "http://auth0.com/oauth/grant-type/password-realm"

_OEM_LOGIN: dict[str, dict[str, str]] = {
    SupportedOEM.EON_HOME: {
        "client_id": "mG0Phmo7DmnvAqO7p6B0WOYBODppY3cc",
        "realm": "eon-home-authentication-db",
        "scope": "email openid offline_access",
        "audience": API_BASE_URL,
    },
    # Shut down at the end of 2025; kept so that old configs still validate.
    "viessmann": {
        "client_id": "oZpr934Ikn8OZOHTJEcrgXkjio0I0Q7b",
        "realm": "viessmann-authentication-db",
        "scope": "email openid",
        "audience": API_BASE_URL,
    },
}


def supported_oems() -> tuple[str, ...]:
    """Return the OEM identifiers :func:`build_login_config` accepts."""
    return tuple(_OEM_LOGIN)


def build_login_config(
    username: str,
    password: str,
    oem: str = SupportedOEM.EON_HOME,
) -> dict[str, Any]:
    """Return a connector config for ``oem`` with the given credentials.

    The result has the same shape as the bundled JSON config files and can be
    passed to :class:`~gridx_connector.AsyncGridboxConnector` or
    :class:`~gridx_connector.GridboxConnector` unchanged.

    Raises:
        ValueError: If ``oem`` is unknown.
    """
    try:
        login = _OEM_LOGIN[oem]
    except KeyError:
        raise ValueError(f"Unknown OEM {oem!r}; supported: {', '.join(_OEM_LOGIN)}") from None
    if oem == "viessmann":
        warnings.warn(
            "The Viessmann realm was shut down at end of 2025. Support for 'viessmann' OEM is deprecated.",
            DeprecationWarning,
            stacklevel=2,
        )
    return {
        "urls": {"login": LOGIN_URL},
        "login": {
            "grant_type": _GRANT_TYPE,
            "username": username,
            "password": password,
            "audience": login["audience"],
            "client_id": login["client_id"],
            "scope": login["scope"],
            "realm": login["realm"],
            "client_secret": "",
        },
    }
