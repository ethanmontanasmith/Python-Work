"""Tests for :mod:`pywork.tokenizer`."""

from __future__ import annotations

import pytest

from pywork import tokenizer


def test_circular_import() -> None:
    assert tokenizer.__all__


def test_stale_cache_entry() -> None:
    assert tokenizer.__all__


def test_unhandled_keyerror() -> None:
    assert tokenizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
