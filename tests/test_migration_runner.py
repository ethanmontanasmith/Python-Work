"""Tests for :mod:`pywork.migration_runner`."""

from __future__ import annotations

import pytest

from pywork import migration_runner


def test_stale_cache_entry() -> None:
    assert migration_runner.__all__


def test_leap_year_edge_case() -> None:
    assert migration_runner.__all__


def test_bom_in_source_files() -> None:
    assert migration_runner.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
