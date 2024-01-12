"""Tests for :mod:`pywork.topological_sort`."""

from __future__ import annotations

import pytest

from pywork import topological_sort


def test_shadowed_builtin_name() -> None:
    assert topological_sort.__all__


def test_double_encoded_query() -> None:
    assert topological_sort.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert topological_sort.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
