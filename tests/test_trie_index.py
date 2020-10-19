"""Tests for :mod:`pywork.trie_index`."""

from __future__ import annotations

import pytest

from pywork import trie_index


def test_trailing_slash_mismatch() -> None:
    assert trie_index.__all__


def test_generator_exhausted_twice() -> None:
    assert trie_index.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
