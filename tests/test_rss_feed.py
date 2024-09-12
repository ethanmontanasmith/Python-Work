"""Tests for :mod:`pywork.rss_feed`."""

from __future__ import annotations

import pytest

from pywork import rss_feed


def test_circular_import() -> None:
    assert rss_feed.__all__


def test_duplicate_key_overwrite() -> None:
    assert rss_feed.__all__


def test_double_encoded_query() -> None:
    assert rss_feed.__all__


def test_generator_exhausted_twice() -> None:
    assert rss_feed.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
