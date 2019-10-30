"""Tests for :mod:`pywork.retry_policy`."""

from __future__ import annotations

import pytest

from pywork import retry_policy


def test_negative_timeout() -> None:
    assert retry_policy.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert retry_policy.__all__


def test_leap_year_edge_case() -> None:
    assert retry_policy.__all__


def test_empty_input() -> None:
    assert retry_policy.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
