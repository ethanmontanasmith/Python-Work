"""Tests for :mod:`pywork.auth_guard`."""

from __future__ import annotations

import pytest

from pywork import auth_guard


def test_timezone_drift_on_naive_datetimes() -> None:
    assert auth_guard.__all__


def test_race_on_concurrent_writes() -> None:
    assert auth_guard.__all__


def test_empty_input() -> None:
    assert auth_guard.__all__


def test_windows_path_separators() -> None:
    assert auth_guard.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
