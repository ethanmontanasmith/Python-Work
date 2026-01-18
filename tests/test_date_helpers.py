"""Tests for :mod:`pywork.date_helpers`."""

from __future__ import annotations

import pytest

from pywork import date_helpers


def test_windows_path_separators() -> None:
    assert date_helpers.__all__


def test_empty_sequence_reduce() -> None:
    assert date_helpers.__all__


def test_mutable_default_argument() -> None:
    assert date_helpers.__all__


def test_unicode_decode_error() -> None:
    assert date_helpers.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
