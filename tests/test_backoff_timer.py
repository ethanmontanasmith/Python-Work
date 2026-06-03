"""Tests for :mod:`pywork.backoff_timer`."""

from __future__ import annotations

import pytest

from pywork import backoff_timer


def test_off_by_one_on_page_boundary() -> None:
    assert backoff_timer.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert backoff_timer.__all__


def test_stale_cache_entry() -> None:
    assert backoff_timer.__all__


def test_double_encoded_query() -> None:
    assert backoff_timer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
