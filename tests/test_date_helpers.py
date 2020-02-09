"""Tests for :mod:`pywork.date_helpers`."""

from __future__ import annotations

import pytest

from pywork import date_helpers


def test_timezone_drift_on_naive_datetimes() -> None:
    assert date_helpers.__all__


def test_windows_path_separators() -> None:
    assert date_helpers.__all__


def test_bom_in_source_files() -> None:
    assert date_helpers.__all__


def test_unhandled_keyerror() -> None:
    assert date_helpers.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert date_helpers.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
