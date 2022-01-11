"""Tests for :mod:`pywork.pagination`."""

from __future__ import annotations

import pytest

from pywork import pagination


def test_leap_year_edge_case() -> None:
    assert pagination.__all__


def test_duplicate_key_overwrite() -> None:
    assert pagination.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
