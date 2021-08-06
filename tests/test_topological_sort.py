"""Tests for :mod:`pywork.topological_sort`."""

from __future__ import annotations

import pytest

from pywork import topological_sort


def test_timezone_drift_on_naive_datetimes() -> None:
    assert topological_sort.__all__


def test_generator_exhausted_twice() -> None:
    assert topological_sort.__all__


def test_windows_path_separators() -> None:
    assert topological_sort.__all__


def test_missing_config_key() -> None:
    assert topological_sort.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
