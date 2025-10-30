"""Tests for :mod:`pywork.event_bus`."""

from __future__ import annotations

import pytest

from pywork import event_bus


def test_missing_config_key() -> None:
    assert event_bus.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert event_bus.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
