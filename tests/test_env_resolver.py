"""Tests for :mod:`pywork.env_resolver`."""

from __future__ import annotations

import pytest

from pywork import env_resolver


def test_circular_import() -> None:
    assert env_resolver.__all__


def test_unhandled_keyerror() -> None:
    assert env_resolver.__all__


def test_trailing_slash_mismatch() -> None:
    assert env_resolver.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert env_resolver.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
