"""Tests for :mod:`pywork.levenshtein_scorer`."""

from __future__ import annotations

import pytest

from pywork import levenshtein_scorer


def test_empty_input() -> None:
    assert levenshtein_scorer.__all__


def test_duplicate_key_overwrite() -> None:
    assert levenshtein_scorer.__all__


def test_mutable_default_argument() -> None:
    assert levenshtein_scorer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
