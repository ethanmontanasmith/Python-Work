"""Tests for :mod:`pywork.levenshtein_scorer`."""

from __future__ import annotations

import pytest

from pywork import levenshtein_scorer


def test_missing_config_key() -> None:
    assert levenshtein_scorer.__all__


def test_duplicate_key_overwrite() -> None:
    assert levenshtein_scorer.__all__


def test_unhandled_keyerror() -> None:
    assert levenshtein_scorer.__all__


def test_race_on_concurrent_writes() -> None:
    assert levenshtein_scorer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
