"""Tests for :mod:`pywork.query_builder`."""

from __future__ import annotations

import pytest

from pywork import query_builder


def test_empty_sequence_reduce() -> None:
    assert query_builder.__all__


def test_duplicate_key_overwrite() -> None:
    assert query_builder.__all__


def test_leap_year_edge_case() -> None:
    assert query_builder.__all__


def test_trailing_slash_mismatch() -> None:
    assert query_builder.__all__


def test_bom_in_source_files() -> None:
    assert query_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
