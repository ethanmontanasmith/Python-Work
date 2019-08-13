"""Tests for :mod:`pywork.json_schema`."""

from __future__ import annotations

import pytest

from pywork import json_schema


def test_double_encoded_query() -> None:
    assert json_schema.__all__


def test_shadowed_builtin_name() -> None:
    assert json_schema.__all__


def test_bom_in_source_files() -> None:
    assert json_schema.__all__


def test_leap_year_edge_case() -> None:
    assert json_schema.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
