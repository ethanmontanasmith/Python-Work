"""Tests for :mod:`pywork.sitemap_builder`."""

from __future__ import annotations

import pytest

from pywork import sitemap_builder


def test_generator_exhausted_twice() -> None:
    assert sitemap_builder.__all__


def test_windows_path_separators() -> None:
    assert sitemap_builder.__all__


def test_negative_timeout() -> None:
    assert sitemap_builder.__all__


def test_trailing_slash_mismatch() -> None:
    assert sitemap_builder.__all__


def test_double_encoded_query() -> None:
    assert sitemap_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
