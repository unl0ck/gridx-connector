"""Tests for SupportedOEM."""

import warnings

from gridx_connector.supported_oem import SupportedOEM


def test_eon_home_value():
    assert SupportedOEM.EON_HOME == "eon-home"


def test_viessmann_returns_correct_string():
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        assert SupportedOEM.VIESSMANN == "viessmann"


def test_viessmann_triggers_deprecation_warning():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        _ = SupportedOEM.VIESSMANN
    assert len(w) == 1
    assert issubclass(w[0].category, DeprecationWarning)
    assert "Viessmann" in str(w[0].message)


def test_eon_home_does_not_warn():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        _ = SupportedOEM.EON_HOME
    deprecations = [x for x in w if issubclass(x.category, DeprecationWarning)]
    assert len(deprecations) == 0
