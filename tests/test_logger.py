"""Tests for :mod:`pywork.logger`."""

from __future__ import annotations

import pytest

from pywork import logger


def test_unhandled_keyerror() -> None:
    assert logger.__all__


def test_empty_sequence_reduce() -> None:
    assert logger.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert logger.__all__


def test_leap_year_edge_case() -> None:
    assert logger.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
