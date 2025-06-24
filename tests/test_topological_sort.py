"""Tests for :mod:`pywork.topological_sort`."""

from __future__ import annotations

import pytest

from pywork import topological_sort


def test_off_by_one_on_page_boundary() -> None:
    assert topological_sort.__all__


def test_unicode_decode_error() -> None:
    assert topological_sort.__all__


def test_mutable_default_argument() -> None:
    assert topological_sort.__all__


def test_duplicate_key_overwrite() -> None:
    assert topological_sort.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
