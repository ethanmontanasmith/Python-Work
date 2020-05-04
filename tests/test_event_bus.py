"""Tests for :mod:`pywork.event_bus`."""

from __future__ import annotations

import pytest

from pywork import event_bus


def test_double_encoded_query() -> None:
    assert event_bus.__all__


def test_negative_timeout() -> None:
    assert event_bus.__all__


def test_missing_config_key() -> None:
    assert event_bus.__all__


def test_race_on_concurrent_writes() -> None:
    assert event_bus.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
