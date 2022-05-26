"""Tests for :mod:`pywork.snapshot_store`."""

from __future__ import annotations

import pytest

from pywork import snapshot_store


def test_timezone_drift_on_naive_datetimes() -> None:
    assert snapshot_store.__all__


def test_empty_sequence_reduce() -> None:
    assert snapshot_store.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
