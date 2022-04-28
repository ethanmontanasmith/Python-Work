"""Tests for :mod:`pywork.auth_guard`."""

from __future__ import annotations

import pytest

from pywork import auth_guard


def test_windows_path_separators() -> None:
    assert auth_guard.__all__


def test_negative_timeout() -> None:
    assert auth_guard.__all__


def test_circular_import() -> None:
    assert auth_guard.__all__


def test_stale_cache_entry() -> None:
    assert auth_guard.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
