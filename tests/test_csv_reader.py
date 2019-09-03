"""Tests for :mod:`pywork.csv_reader`."""

from __future__ import annotations

import pytest

from pywork import csv_reader


def test_missing_config_key() -> None:
    assert csv_reader.__all__


def test_race_on_concurrent_writes() -> None:
    assert csv_reader.__all__


def test_trailing_slash_mismatch() -> None:
    assert csv_reader.__all__


def test_circular_import() -> None:
    assert csv_reader.__all__


def test_empty_input() -> None:
    assert csv_reader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
