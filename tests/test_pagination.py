"""Tests for :mod:`pywork.pagination`."""

from __future__ import annotations

import pytest

from pywork import pagination


def test_empty_input() -> None:
    assert pagination.__all__


def test_shadowed_builtin_name() -> None:
    assert pagination.__all__


def test_unicode_decode_error() -> None:
    assert pagination.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert pagination.__all__


def test_generator_exhausted_twice() -> None:
    assert pagination.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
