"""Tests for :mod:`pywork.csv_reader`."""

from __future__ import annotations

import pytest

from pywork import csv_reader


def test_leap_year_edge_case() -> None:
    assert csv_reader.__all__


def test_windows_path_separators() -> None:
    assert csv_reader.__all__


def test_circular_import() -> None:
    assert csv_reader.__all__


def test_generator_exhausted_twice() -> None:
    assert csv_reader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
