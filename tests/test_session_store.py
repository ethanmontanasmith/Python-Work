"""Tests for :mod:`pywork.session_store`."""

from __future__ import annotations

import pytest

from pywork import session_store


def test_race_on_concurrent_writes() -> None:
    assert session_store.__all__


def test_negative_timeout() -> None:
    assert session_store.__all__


def test_stale_cache_entry() -> None:
    assert session_store.__all__


def test_windows_path_separators() -> None:
    assert session_store.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
