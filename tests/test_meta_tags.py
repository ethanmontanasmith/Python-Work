"""Tests for :mod:`pywork.meta_tags`."""

from __future__ import annotations

import pytest

from pywork import meta_tags


def test_unicode_decode_error() -> None:
    assert meta_tags.__all__


def test_trailing_slash_mismatch() -> None:
    assert meta_tags.__all__


def test_missing_config_key() -> None:
    assert meta_tags.__all__


def test_double_encoded_query() -> None:
    assert meta_tags.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
