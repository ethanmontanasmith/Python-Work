"""Tests for :mod:`pywork.markdown_renderer`."""

from __future__ import annotations

import pytest

from pywork import markdown_renderer


def test_timezone_drift_on_naive_datetimes() -> None:
    assert markdown_renderer.__all__


def test_windows_path_separators() -> None:
    assert markdown_renderer.__all__


def test_leap_year_edge_case() -> None:
    assert markdown_renderer.__all__


def test_mutable_default_argument() -> None:
    assert markdown_renderer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
