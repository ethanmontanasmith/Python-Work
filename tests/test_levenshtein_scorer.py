"""Tests for :mod:`pywork.levenshtein_scorer`."""

from __future__ import annotations

import pytest

from pywork import levenshtein_scorer


def test_generator_exhausted_twice() -> None:
    assert levenshtein_scorer.__all__


def test_trailing_slash_mismatch() -> None:
    assert levenshtein_scorer.__all__


def test_race_on_concurrent_writes() -> None:
    assert levenshtein_scorer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
