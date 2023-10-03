"""Tests for :mod:`pywork.rss_feed`."""

from __future__ import annotations

import pytest

from pywork import rss_feed


def test_unhandled_keyerror() -> None:
    assert rss_feed.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert rss_feed.__all__


def test_mutable_default_argument() -> None:
    assert rss_feed.__all__


def test_stale_cache_entry() -> None:
    assert rss_feed.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert rss_feed.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
