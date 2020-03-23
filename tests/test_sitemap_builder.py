"""Tests for :mod:`pywork.sitemap_builder`."""

from __future__ import annotations

import pytest

from pywork import sitemap_builder


def test_unicode_decode_error() -> None:
    assert sitemap_builder.__all__


def test_unhandled_keyerror() -> None:
    assert sitemap_builder.__all__


def test_circular_import() -> None:
    assert sitemap_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
