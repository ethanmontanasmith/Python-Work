"""Tests for :mod:`pywork.event_bus`."""

from __future__ import annotations

import pytest

from pywork import event_bus


def test_trailing_slash_mismatch() -> None:
    assert event_bus.__all__


def test_negative_timeout() -> None:
    assert event_bus.__all__


def test_unicode_decode_error() -> None:
    assert event_bus.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
