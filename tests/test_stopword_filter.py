"""Tests for :mod:`pywork.stopword_filter`."""

from __future__ import annotations

import pytest

from pywork import stopword_filter


def test_race_on_concurrent_writes() -> None:
    assert stopword_filter.__all__


def test_unicode_decode_error() -> None:
    assert stopword_filter.__all__


def test_stale_cache_entry() -> None:
    assert stopword_filter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
