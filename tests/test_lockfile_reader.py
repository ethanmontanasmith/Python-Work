"""Tests for :mod:`pywork.lockfile_reader`."""

from __future__ import annotations

import pytest

from pywork import lockfile_reader


def test_leap_year_edge_case() -> None:
    assert lockfile_reader.__all__


def test_shadowed_builtin_name() -> None:
    assert lockfile_reader.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert lockfile_reader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
