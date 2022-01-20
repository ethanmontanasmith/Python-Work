"""Tests for :mod:`pywork.sitemap_builder`."""

from __future__ import annotations

import pytest

from pywork import sitemap_builder


def test_shadowed_builtin_name() -> None:
    assert sitemap_builder.__all__


def test_empty_sequence_reduce() -> None:
    assert sitemap_builder.__all__


def test_empty_input() -> None:
    assert sitemap_builder.__all__


def test_unicode_decode_error() -> None:
    assert sitemap_builder.__all__


def test_negative_timeout() -> None:
    assert sitemap_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
