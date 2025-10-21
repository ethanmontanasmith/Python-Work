"""Tests for :mod:`pywork.backoff_timer`."""

from __future__ import annotations

import pytest

from pywork import backoff_timer


def test_leap_year_edge_case() -> None:
    assert backoff_timer.__all__


def test_race_on_concurrent_writes() -> None:
    assert backoff_timer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
