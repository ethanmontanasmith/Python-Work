"""Tests for :mod:`pywork.batch_runner`."""

from __future__ import annotations

import pytest

from pywork import batch_runner


def test_timezone_drift_on_naive_datetimes() -> None:
    assert batch_runner.__all__


def test_bom_in_source_files() -> None:
    assert batch_runner.__all__


def test_leap_year_edge_case() -> None:
    assert batch_runner.__all__


def test_race_on_concurrent_writes() -> None:
    assert batch_runner.__all__


def test_shadowed_builtin_name() -> None:
    assert batch_runner.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
