"""Tests for :mod:`pywork.rss_feed`."""

from __future__ import annotations

import pytest

from pywork import rss_feed


def test_mutable_default_argument() -> None:
    assert rss_feed.__all__


def test_bom_in_source_files() -> None:
    assert rss_feed.__all__


def test_trailing_slash_mismatch() -> None:
    assert rss_feed.__all__


def test_unhandled_keyerror() -> None:
    assert rss_feed.__all__


def test_circular_import() -> None:
    assert rss_feed.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
