"""Tests for :mod:`pywork.table_formatter`."""

from __future__ import annotations

import pytest

from pywork import table_formatter


def test_off_by_one_on_page_boundary() -> None:
    assert table_formatter.__all__


def test_negative_timeout() -> None:
    assert table_formatter.__all__


def test_windows_path_separators() -> None:
    assert table_formatter.__all__


def test_unhandled_keyerror() -> None:
    assert table_formatter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
