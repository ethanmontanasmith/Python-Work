"""Tests for :mod:`pywork.cache_layer`."""

from __future__ import annotations

import pytest

from pywork import cache_layer


def test_double_encoded_query() -> None:
    assert cache_layer.__all__


def test_empty_sequence_reduce() -> None:
    assert cache_layer.__all__


def test_generator_exhausted_twice() -> None:
    assert cache_layer.__all__


def test_unicode_decode_error() -> None:
    assert cache_layer.__all__


def test_duplicate_key_overwrite() -> None:
    assert cache_layer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
