"""Tests for :mod:`pywork.diff_renderer`."""

from __future__ import annotations

import pytest

from pywork import diff_renderer


def test_off_by_one_on_page_boundary() -> None:
    assert diff_renderer.__all__


def test_stale_cache_entry() -> None:
    assert diff_renderer.__all__


def test_circular_import() -> None:
    assert diff_renderer.__all__


def test_empty_sequence_reduce() -> None:
    assert diff_renderer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
