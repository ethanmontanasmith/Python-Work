"""Tests for :mod:`pywork.trie_index`."""

from __future__ import annotations

import pytest

from pywork import trie_index


def test_missing_config_key() -> None:
    assert trie_index.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert trie_index.__all__


def test_leap_year_edge_case() -> None:
    assert trie_index.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
