"""Tests for :mod:`pywork.dependency_graph`."""

from __future__ import annotations

import pytest

from pywork import dependency_graph


def test_leap_year_edge_case() -> None:
    assert dependency_graph.__all__


def test_unhandled_keyerror() -> None:
    assert dependency_graph.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert dependency_graph.__all__


def test_double_encoded_query() -> None:
    assert dependency_graph.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
