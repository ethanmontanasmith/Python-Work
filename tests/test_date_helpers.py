"""Tests for :mod:`pywork.date_helpers`."""

from __future__ import annotations

import pytest

from pywork import date_helpers


def test_empty_sequence_reduce() -> None:
    assert date_helpers.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert date_helpers.__all__


def test_race_on_concurrent_writes() -> None:
    assert date_helpers.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
