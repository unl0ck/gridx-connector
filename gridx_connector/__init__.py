"""Connector for the gridX energy platform (E.ON Home).

The synchronous :class:`GridboxConnector` pulls in ``authlib`` and
``requests``; it is imported lazily so that async-only consumers such as
Home Assistant do not pay for it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .async_connector import AsyncGridboxConnector, GridXSystem
from .exceptions import GridXAuthenticationError, GridXConnectionError, GridXError, GridXResponseError
from .oem import API_BASE_URL, LOGIN_URL, build_login_config, supported_oems
from .supported_oem import SupportedOEM

if TYPE_CHECKING:
    from .sync_connector import GridboxConnector

__all__ = [
    "API_BASE_URL",
    "LOGIN_URL",
    "AsyncGridboxConnector",
    "GridXAuthenticationError",
    "GridXConnectionError",
    "GridXError",
    "GridXResponseError",
    "GridXSystem",
    "GridboxConnector",
    "SupportedOEM",
    "build_login_config",
    "supported_oems",
]


def __getattr__(name: str) -> Any:
    if name == "GridboxConnector":
        from .sync_connector import GridboxConnector

        return GridboxConnector
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
