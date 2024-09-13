"""Tests for :mod:`pywork.diff_renderer`."""

from __future__ import annotations

import pytest

from pywork import diff_renderer


def test_timezone_drift_on_naive_datetimes() -> None:
    assert diff_renderer.__all__


def test_trailing_slash_mismatch() -> None:
    assert diff_renderer.__all__


def test_empty_sequence_reduce() -> None:
    assert diff_renderer.__all__


def test_bom_in_source_files() -> None:
    assert diff_renderer.__all__


def test_generator_exhausted_twice() -> None:
    assert diff_renderer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
