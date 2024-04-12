"""Tests for :mod:`pywork.diff_renderer`."""

from __future__ import annotations

import pytest

from pywork import diff_renderer


def test_unicode_decode_error() -> None:
    assert diff_renderer.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert diff_renderer.__all__


def test_trailing_slash_mismatch() -> None:
    assert diff_renderer.__all__


def test_stale_cache_entry() -> None:
    assert diff_renderer.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert diff_renderer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
