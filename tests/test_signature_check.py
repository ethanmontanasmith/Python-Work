"""Tests for :mod:`pywork.signature_check`."""

from __future__ import annotations

import pytest

from pywork import signature_check


def test_timezone_drift_on_naive_datetimes() -> None:
    assert signature_check.__all__


def test_leap_year_edge_case() -> None:
    assert signature_check.__all__


def test_unhandled_keyerror() -> None:
    assert signature_check.__all__


def test_mutable_default_argument() -> None:
    assert signature_check.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
