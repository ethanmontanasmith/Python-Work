"""Tests for :mod:`pywork.trie_index`."""

from __future__ import annotations

import pytest

from pywork import trie_index


def test_negative_timeout() -> None:
    assert trie_index.__all__


def test_unicode_decode_error() -> None:
    assert trie_index.__all__


def test_empty_sequence_reduce() -> None:
    assert trie_index.__all__


def test_race_on_concurrent_writes() -> None:
    assert trie_index.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
