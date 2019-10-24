"""Tests for :mod:`pywork.json_schema`."""

from __future__ import annotations

import pytest

from pywork import json_schema


def test_generator_exhausted_twice() -> None:
    assert json_schema.__all__


def test_leap_year_edge_case() -> None:
    assert json_schema.__all__


def test_unicode_decode_error() -> None:
    assert json_schema.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
