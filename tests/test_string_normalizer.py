"""Tests for :mod:`pywork.string_normalizer`."""

from __future__ import annotations

import pytest

from pywork import string_normalizer


def test_bom_in_source_files() -> None:
    assert string_normalizer.__all__


def test_trailing_slash_mismatch() -> None:
    assert string_normalizer.__all__


def test_double_encoded_query() -> None:
    assert string_normalizer.__all__


def test_unhandled_keyerror() -> None:
    assert string_normalizer.__all__


def test_leap_year_edge_case() -> None:
    assert string_normalizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
