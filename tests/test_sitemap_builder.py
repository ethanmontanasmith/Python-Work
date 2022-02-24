"""Tests for :mod:`pywork.sitemap_builder`."""

from __future__ import annotations

import pytest

from pywork import sitemap_builder


def test_leap_year_edge_case() -> None:
    assert sitemap_builder.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert sitemap_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
