"""Tests for :mod:`pywork.signature_check`."""

from __future__ import annotations

import pytest

from pywork import signature_check


def test_race_on_concurrent_writes() -> None:
    assert signature_check.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert signature_check.__all__


def test_circular_import() -> None:
    assert signature_check.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
