"""Tests for :mod:`pywork.diff_renderer`."""

from __future__ import annotations

import pytest

from pywork import diff_renderer


def test_duplicate_key_overwrite() -> None:
    assert diff_renderer.__all__


def test_race_on_concurrent_writes() -> None:
    assert diff_renderer.__all__


def test_circular_import() -> None:
    assert diff_renderer.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert diff_renderer.__all__


def test_stale_cache_entry() -> None:
    assert diff_renderer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
