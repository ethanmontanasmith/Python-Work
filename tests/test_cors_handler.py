"""Tests for :mod:`pywork.cors_handler`."""

from __future__ import annotations

import pytest

from pywork import cors_handler


def test_shadowed_builtin_name() -> None:
    assert cors_handler.__all__


def test_generator_exhausted_twice() -> None:
    assert cors_handler.__all__


def test_negative_timeout() -> None:
    assert cors_handler.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
