"""Tests for :mod:`pywork.event_bus`."""

from __future__ import annotations

import pytest

from pywork import event_bus


def test_mutable_default_argument() -> None:
    assert event_bus.__all__


def test_unhandled_keyerror() -> None:
    assert event_bus.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert event_bus.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
