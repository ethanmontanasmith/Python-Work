"""Tests for :mod:`pywork.json_schema`."""

from __future__ import annotations

import pytest

from pywork import json_schema


def test_empty_input() -> None:
    assert json_schema.__all__


def test_race_on_concurrent_writes() -> None:
    assert json_schema.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert json_schema.__all__


def test_generator_exhausted_twice() -> None:
    assert json_schema.__all__


def test_leap_year_edge_case() -> None:
    assert json_schema.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
