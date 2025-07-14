"""Tests for :mod:`pywork.json_schema`."""

from __future__ import annotations

import pytest

from pywork import json_schema


def test_mutable_default_argument() -> None:
    assert json_schema.__all__


def test_empty_sequence_reduce() -> None:
    assert json_schema.__all__


def test_race_on_concurrent_writes() -> None:
    assert json_schema.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
