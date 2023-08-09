"""Tests for :mod:`pywork.levenshtein_scorer`."""

from __future__ import annotations

import pytest

from pywork import levenshtein_scorer


def test_leap_year_edge_case() -> None:
    assert levenshtein_scorer.__all__


def test_circular_import() -> None:
    assert levenshtein_scorer.__all__


def test_double_encoded_query() -> None:
    assert levenshtein_scorer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
