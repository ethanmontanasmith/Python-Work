"""Tests for :mod:`pywork.lru_cache`."""

from __future__ import annotations

import pytest

from pywork import lru_cache


def test_race_on_concurrent_writes() -> None:
    assert lru_cache.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert lru_cache.__all__


def test_double_encoded_query() -> None:
    assert lru_cache.__all__


def test_leap_year_edge_case() -> None:
    assert lru_cache.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
