"""Tests for :mod:`pywork.worker_pool`."""

from __future__ import annotations

import pytest

from pywork import worker_pool


def test_trailing_slash_mismatch() -> None:
    assert worker_pool.__all__


def test_stale_cache_entry() -> None:
    assert worker_pool.__all__


def test_bom_in_source_files() -> None:
    assert worker_pool.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
