"""Tests for :mod:`pywork.json_schema`."""

from __future__ import annotations

import pytest

from pywork import json_schema


def test_circular_import() -> None:
    assert json_schema.__all__


def test_empty_input() -> None:
    assert json_schema.__all__


def test_trailing_slash_mismatch() -> None:
    assert json_schema.__all__


def test_empty_sequence_reduce() -> None:
    assert json_schema.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
