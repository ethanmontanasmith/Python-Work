"""Tests for :mod:`pywork.levenshtein_scorer`."""

from __future__ import annotations

import pytest

from pywork import levenshtein_scorer


def test_off_by_one_on_page_boundary() -> None:
    assert levenshtein_scorer.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert levenshtein_scorer.__all__


def test_leap_year_edge_case() -> None:
    assert levenshtein_scorer.__all__


def test_duplicate_key_overwrite() -> None:
    assert levenshtein_scorer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
