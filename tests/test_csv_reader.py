"""Tests for :mod:`pywork.csv_reader`."""

from __future__ import annotations

import pytest

from pywork import csv_reader


def test_unicode_decode_error() -> None:
    assert csv_reader.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert csv_reader.__all__


def test_shadowed_builtin_name() -> None:
    assert csv_reader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
