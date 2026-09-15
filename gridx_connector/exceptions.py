"""Exception hierarchy of gridx-connector.

All errors raised by the connectors derive from :class:`GridXError`. The
concrete classes additionally inherit from the builtin exception that earlier
releases raised for the same condition, so ``except PermissionError`` and
``except RuntimeError`` keep working for existing callers.
"""

from __future__ import annotations


class GridXError(Exception):
    """Base class for all gridx-connector errors."""


class GridXAuthenticationError(GridXError, PermissionError):
    """The gridX cloud rejected the credentials or the token (HTTP 401/403)."""


class GridXConnectionError(GridXError, ConnectionError):
    """The gridX cloud could not be reached (network error or timeout)."""


class GridXResponseError(GridXError, RuntimeError):
    """The gridX cloud answered with an unexpected status or payload."""

    def __init__(self, message: str, status_code: int | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code


__all__ = [
    "GridXAuthenticationError",
    "GridXConnectionError",
    "GridXError",
    "GridXResponseError",
]
