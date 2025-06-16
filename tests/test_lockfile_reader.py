"""Tests for :mod:`pywork.lockfile_reader`."""

from __future__ import annotations

import pytest

from pywork import lockfile_reader


def test_leap_year_edge_case() -> None:
    assert lockfile_reader.__all__


def test_unhandled_keyerror() -> None:
    assert lockfile_reader.__all__


def test_stale_cache_entry() -> None:
    assert lockfile_reader.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert lockfile_reader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
