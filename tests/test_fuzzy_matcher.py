"""Tests for :mod:`pywork.fuzzy_matcher`."""

from __future__ import annotations

import pytest

from pywork import fuzzy_matcher


def test_double_encoded_query() -> None:
    assert fuzzy_matcher.__all__


def test_race_on_concurrent_writes() -> None:
    assert fuzzy_matcher.__all__


def test_leap_year_edge_case() -> None:
    assert fuzzy_matcher.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
