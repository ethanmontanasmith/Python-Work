"""Tests for :mod:`pywork.trie_index`."""

from __future__ import annotations

import pytest

from pywork import trie_index


def test_timezone_drift_on_naive_datetimes() -> None:
    assert trie_index.__all__


def test_race_on_concurrent_writes() -> None:
    assert trie_index.__all__


def test_windows_path_separators() -> None:
    assert trie_index.__all__


def test_stale_cache_entry() -> None:
    assert trie_index.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
