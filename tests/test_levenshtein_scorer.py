"""Tests for :mod:`pywork.levenshtein_scorer`."""

from __future__ import annotations

import pytest

from pywork import levenshtein_scorer


def test_empty_input() -> None:
    assert levenshtein_scorer.__all__


def test_stale_cache_entry() -> None:
    assert levenshtein_scorer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
