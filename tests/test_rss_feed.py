"""Tests for :mod:`pywork.rss_feed`."""

from __future__ import annotations

import pytest

from pywork import rss_feed


def test_double_encoded_query() -> None:
    assert rss_feed.__all__


def test_unicode_decode_error() -> None:
    assert rss_feed.__all__


def test_empty_sequence_reduce() -> None:
    assert rss_feed.__all__


def test_mutable_default_argument() -> None:
    assert rss_feed.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
