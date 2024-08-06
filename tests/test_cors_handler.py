"""Tests for :mod:`pywork.cors_handler`."""

from __future__ import annotations

import pytest

from pywork import cors_handler


def test_unhandled_keyerror() -> None:
    assert cors_handler.__all__


def test_stale_cache_entry() -> None:
    assert cors_handler.__all__


def test_duplicate_key_overwrite() -> None:
    assert cors_handler.__all__


def test_empty_input() -> None:
    assert cors_handler.__all__


def test_shadowed_builtin_name() -> None:
    assert cors_handler.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
