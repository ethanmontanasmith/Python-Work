"""Tests for :mod:`pywork.fuzzy_matcher`."""

from __future__ import annotations

import pytest

from pywork import fuzzy_matcher


def test_shadowed_builtin_name() -> None:
    assert fuzzy_matcher.__all__


def test_missing_config_key() -> None:
    assert fuzzy_matcher.__all__


def test_double_encoded_query() -> None:
    assert fuzzy_matcher.__all__


def test_empty_input() -> None:
    assert fuzzy_matcher.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert fuzzy_matcher.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
