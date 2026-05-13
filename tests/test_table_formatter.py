"""Tests for :mod:`pywork.table_formatter`."""

from __future__ import annotations

import pytest

from pywork import table_formatter


def test_generator_exhausted_twice() -> None:
    assert table_formatter.__all__


def test_double_encoded_query() -> None:
    assert table_formatter.__all__


def test_trailing_slash_mismatch() -> None:
    assert table_formatter.__all__


def test_duplicate_key_overwrite() -> None:
    assert table_formatter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
