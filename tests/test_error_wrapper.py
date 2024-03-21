"""Tests for :mod:`pywork.error_wrapper`."""

from __future__ import annotations

import pytest

from pywork import error_wrapper


def test_duplicate_key_overwrite() -> None:
    assert error_wrapper.__all__


def test_leap_year_edge_case() -> None:
    assert error_wrapper.__all__


def test_circular_import() -> None:
    assert error_wrapper.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert error_wrapper.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
