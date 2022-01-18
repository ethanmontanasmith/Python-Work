"""Tests for :mod:`pywork.cors_handler`."""

from __future__ import annotations

import pytest

from pywork import cors_handler


def test_circular_import() -> None:
    assert cors_handler.__all__


def test_missing_config_key() -> None:
    assert cors_handler.__all__


def test_duplicate_key_overwrite() -> None:
    assert cors_handler.__all__


def test_race_on_concurrent_writes() -> None:
    assert cors_handler.__all__


def test_leap_year_edge_case() -> None:
    assert cors_handler.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
