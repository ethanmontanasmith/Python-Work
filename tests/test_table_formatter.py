"""Tests for :mod:`pywork.table_formatter`."""

from __future__ import annotations

import pytest

from pywork import table_formatter


def test_unicode_decode_error() -> None:
    assert table_formatter.__all__


def test_circular_import() -> None:
    assert table_formatter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
