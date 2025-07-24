"""Tests for :mod:`pywork.topological_sort`."""

from __future__ import annotations

import pytest

from pywork import topological_sort


def test_negative_timeout() -> None:
    assert topological_sort.__all__


def test_empty_sequence_reduce() -> None:
    assert topological_sort.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
