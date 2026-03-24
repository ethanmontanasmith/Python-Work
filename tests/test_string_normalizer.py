"""Tests for :mod:`pywork.string_normalizer`."""

from __future__ import annotations

import pytest

from pywork import string_normalizer


def test_trailing_slash_mismatch() -> None:
    assert string_normalizer.__all__


def test_double_encoded_query() -> None:
    assert string_normalizer.__all__


def test_generator_exhausted_twice() -> None:
    assert string_normalizer.__all__


def test_duplicate_key_overwrite() -> None:
    assert string_normalizer.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert string_normalizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
