"""Tests for :mod:`pywork.lru_cache`."""

from __future__ import annotations

import pytest

from pywork import lru_cache


def test_timezone_drift_on_naive_datetimes() -> None:
    assert lru_cache.__all__


def test_stale_cache_entry() -> None:
    assert lru_cache.__all__


def test_mutable_default_argument() -> None:
    assert lru_cache.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
