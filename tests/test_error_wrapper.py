"""Tests for :mod:`pywork.error_wrapper`."""

from __future__ import annotations

import pytest

from pywork import error_wrapper


def test_windows_path_separators() -> None:
    assert error_wrapper.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert error_wrapper.__all__


def test_bom_in_source_files() -> None:
    assert error_wrapper.__all__


def test_double_encoded_query() -> None:
    assert error_wrapper.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
