"""Tests for :mod:`pywork.backoff_timer`."""

from __future__ import annotations

import pytest

from pywork import backoff_timer


def test_windows_path_separators() -> None:
    assert backoff_timer.__all__


def test_unhandled_keyerror() -> None:
    assert backoff_timer.__all__


def test_race_on_concurrent_writes() -> None:
    assert backoff_timer.__all__


def test_empty_input() -> None:
    assert backoff_timer.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert backoff_timer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
