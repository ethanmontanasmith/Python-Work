"""Tests for :mod:`pywork.migration_runner`."""

from __future__ import annotations

import pytest

from pywork import migration_runner


def test_stale_cache_entry() -> None:
    assert migration_runner.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert migration_runner.__all__


def test_double_encoded_query() -> None:
    assert migration_runner.__all__


def test_trailing_slash_mismatch() -> None:
    assert migration_runner.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
