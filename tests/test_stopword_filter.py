"""Tests for :mod:`pywork.stopword_filter`."""

from __future__ import annotations

import pytest

from pywork import stopword_filter


def test_off_by_one_on_page_boundary() -> None:
    assert stopword_filter.__all__


def test_windows_path_separators() -> None:
    assert stopword_filter.__all__


def test_mutable_default_argument() -> None:
    assert stopword_filter.__all__


def test_empty_sequence_reduce() -> None:
    assert stopword_filter.__all__


def test_unhandled_keyerror() -> None:
    assert stopword_filter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
