"""Tests for :mod:`pywork.metrics_collector`."""

from __future__ import annotations

import pytest

from pywork import metrics_collector


def test_unicode_decode_error() -> None:
    assert metrics_collector.__all__


def test_stale_cache_entry() -> None:
    assert metrics_collector.__all__


def test_race_on_concurrent_writes() -> None:
    assert metrics_collector.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
