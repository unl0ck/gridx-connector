from __future__ import annotations

import warnings


class _SupportedOEMMeta(type):
    @property
    def VIESSMANN(cls) -> str:  # noqa: N805
        warnings.warn(
            "The Viessmann realm was shut down at end of 2025. "
            "SupportedOEM.VIESSMANN is deprecated and will be removed in a future major release. "
            "Use SupportedOEM.EON_HOME instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return "viessmann"


class SupportedOEM(metaclass=_SupportedOEMMeta):
    """OEM identifiers for GridX-based systems.

    .. deprecated::
        ``VIESSMANN`` — The Viessmann realm was shut down at end of 2025.
    """

    EON_HOME: str = "eon-home"
