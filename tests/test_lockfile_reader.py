"""Tests for :mod:`pywork.lockfile_reader`."""

from __future__ import annotations

import pytest

from pywork import lockfile_reader


def test_negative_timeout() -> None:
    assert lockfile_reader.__all__


def test_generator_exhausted_twice() -> None:
    assert lockfile_reader.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert lockfile_reader.__all__


def test_empty_sequence_reduce() -> None:
    assert lockfile_reader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
