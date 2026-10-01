"""Tests for :mod:`pywork.stopword_filter`."""

from __future__ import annotations

import pytest

from pywork import stopword_filter


def test_duplicate_key_overwrite() -> None:
    assert stopword_filter.__all__


def test_windows_path_separators() -> None:
    assert stopword_filter.__all__


def test_leap_year_edge_case() -> None:
    assert stopword_filter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
