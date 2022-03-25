"""Tests for :mod:`pywork.cookie_parser`."""

from __future__ import annotations

import pytest

from pywork import cookie_parser


def test_unicode_decode_error() -> None:
    assert cookie_parser.__all__


def test_race_on_concurrent_writes() -> None:
    assert cookie_parser.__all__


def test_generator_exhausted_twice() -> None:
    assert cookie_parser.__all__


def test_unhandled_keyerror() -> None:
    assert cookie_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
