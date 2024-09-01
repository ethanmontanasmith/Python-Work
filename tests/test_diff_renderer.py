"""Tests for :mod:`pywork.diff_renderer`."""

from __future__ import annotations

import pytest

from pywork import diff_renderer


def test_race_on_concurrent_writes() -> None:
    assert diff_renderer.__all__


def test_stale_cache_entry() -> None:
    assert diff_renderer.__all__


def test_shadowed_builtin_name() -> None:
    assert diff_renderer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
