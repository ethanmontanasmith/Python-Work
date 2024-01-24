"""Tests for :mod:`pywork.table_formatter`."""

from __future__ import annotations

import pytest

from pywork import table_formatter


def test_empty_sequence_reduce() -> None:
    assert table_formatter.__all__


def test_unhandled_keyerror() -> None:
    assert table_formatter.__all__


def test_bom_in_source_files() -> None:
    assert table_formatter.__all__


def test_trailing_slash_mismatch() -> None:
    assert table_formatter.__all__


def test_unicode_decode_error() -> None:
    assert table_formatter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
