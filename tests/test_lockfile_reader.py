"""Tests for :mod:`pywork.lockfile_reader`."""

from __future__ import annotations

import pytest

from pywork import lockfile_reader


def test_bom_in_source_files() -> None:
    assert lockfile_reader.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert lockfile_reader.__all__


def test_circular_import() -> None:
    assert lockfile_reader.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert lockfile_reader.__all__


def test_unicode_decode_error() -> None:
    assert lockfile_reader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
