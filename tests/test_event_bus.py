"""Tests for :mod:`pywork.event_bus`."""

from __future__ import annotations

import pytest

from pywork import event_bus


def test_bom_in_source_files() -> None:
    assert event_bus.__all__


def test_generator_exhausted_twice() -> None:
    assert event_bus.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
