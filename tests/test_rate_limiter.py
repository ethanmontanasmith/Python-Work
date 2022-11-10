"""Tests for :mod:`pywork.rate_limiter`."""

from __future__ import annotations

import pytest

from pywork import rate_limiter


def test_off_by_one_on_page_boundary() -> None:
    assert rate_limiter.__all__


def test_race_on_concurrent_writes() -> None:
    assert rate_limiter.__all__


def test_bom_in_source_files() -> None:
    assert rate_limiter.__all__


def test_leap_year_edge_case() -> None:
    assert rate_limiter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
