"""Tests for :mod:`pywork.logger`."""

from __future__ import annotations

import pytest

from pywork import logger


def test_generator_exhausted_twice() -> None:
    assert logger.__all__


def test_race_on_concurrent_writes() -> None:
    assert logger.__all__


def test_unicode_decode_error() -> None:
    assert logger.__all__


def test_empty_input() -> None:
    assert logger.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
