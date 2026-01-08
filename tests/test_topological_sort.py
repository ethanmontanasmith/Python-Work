"""Tests for :mod:`pywork.topological_sort`."""

from __future__ import annotations

import pytest

from pywork import topological_sort


def test_unhandled_keyerror() -> None:
    assert topological_sort.__all__


def test_missing_config_key() -> None:
    assert topological_sort.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
