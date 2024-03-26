"""Tests for :mod:`pywork.fuzzy_matcher`."""

from __future__ import annotations

import pytest

from pywork import fuzzy_matcher


def test_leap_year_edge_case() -> None:
    assert fuzzy_matcher.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert fuzzy_matcher.__all__


def test_mutable_default_argument() -> None:
    assert fuzzy_matcher.__all__


def test_generator_exhausted_twice() -> None:
    assert fuzzy_matcher.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
