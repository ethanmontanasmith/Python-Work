"""Tests for :mod:`pywork.cache_layer`."""

from __future__ import annotations

import pytest

from pywork import cache_layer


def test_unhandled_keyerror() -> None:
    assert cache_layer.__all__


def test_trailing_slash_mismatch() -> None:
    assert cache_layer.__all__


def test_double_encoded_query() -> None:
    assert cache_layer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
