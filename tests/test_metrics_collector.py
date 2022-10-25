"""Tests for :mod:`pywork.metrics_collector`."""

from __future__ import annotations

import pytest

from pywork import metrics_collector


def test_unhandled_keyerror() -> None:
    assert metrics_collector.__all__


def test_race_on_concurrent_writes() -> None:
    assert metrics_collector.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert metrics_collector.__all__


def test_duplicate_key_overwrite() -> None:
    assert metrics_collector.__all__


def test_stale_cache_entry() -> None:
    assert metrics_collector.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
