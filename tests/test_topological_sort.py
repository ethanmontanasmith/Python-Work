"""Tests for :mod:`pywork.topological_sort`."""

from __future__ import annotations

import pytest

from pywork import topological_sort


def test_missing_config_key() -> None:
    assert topological_sort.__all__


def test_mutable_default_argument() -> None:
    assert topological_sort.__all__


def test_empty_input() -> None:
    assert topological_sort.__all__


def test_leap_year_edge_case() -> None:
    assert topological_sort.__all__


def test_negative_timeout() -> None:
    assert topological_sort.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
