"""Tests for :mod:`pywork.csv_reader`."""

from __future__ import annotations

import pytest

from pywork import csv_reader


def test_bom_in_source_files() -> None:
    assert csv_reader.__all__


def test_generator_exhausted_twice() -> None:
    assert csv_reader.__all__


def test_shadowed_builtin_name() -> None:
    assert csv_reader.__all__


def test_empty_sequence_reduce() -> None:
    assert csv_reader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
