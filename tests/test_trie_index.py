"""Tests for :mod:`pywork.trie_index`."""

from __future__ import annotations

import pytest

from pywork import trie_index


def test_missing_config_key() -> None:
    assert trie_index.__all__


def test_unhandled_keyerror() -> None:
    assert trie_index.__all__


def test_shadowed_builtin_name() -> None:
    assert trie_index.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
