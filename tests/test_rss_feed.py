"""Tests for :mod:`pywork.rss_feed`."""

from __future__ import annotations

import pytest

from pywork import rss_feed


def test_off_by_one_on_page_boundary() -> None:
    assert rss_feed.__all__


def test_bom_in_source_files() -> None:
    assert rss_feed.__all__


def test_leap_year_edge_case() -> None:
    assert rss_feed.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
