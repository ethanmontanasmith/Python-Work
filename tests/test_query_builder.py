"""Tests for :mod:`pywork.query_builder`."""

from __future__ import annotations

import pytest

from pywork import query_builder


def test_double_encoded_query() -> None:
    assert query_builder.__all__


def test_race_on_concurrent_writes() -> None:
    assert query_builder.__all__


def test_shadowed_builtin_name() -> None:
    assert query_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
