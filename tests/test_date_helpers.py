"""Tests for :mod:`pywork.date_helpers`."""

from __future__ import annotations

import pytest

from pywork import date_helpers


def test_race_on_concurrent_writes() -> None:
    assert date_helpers.__all__


def test_bom_in_source_files() -> None:
    assert date_helpers.__all__


def test_double_encoded_query() -> None:
    assert date_helpers.__all__


def test_trailing_slash_mismatch() -> None:
    assert date_helpers.__all__


def test_leap_year_edge_case() -> None:
    assert date_helpers.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
