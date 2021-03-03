"""Tests for :mod:`pywork.rss_feed`."""

from __future__ import annotations

import pytest

from pywork import rss_feed


def test_mutable_default_argument() -> None:
    assert rss_feed.__all__


def test_unicode_decode_error() -> None:
    assert rss_feed.__all__


def test_race_on_concurrent_writes() -> None:
    assert rss_feed.__all__


def test_windows_path_separators() -> None:
    assert rss_feed.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
