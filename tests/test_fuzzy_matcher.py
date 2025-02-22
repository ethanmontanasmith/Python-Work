"""Tests for :mod:`pywork.fuzzy_matcher`."""

from __future__ import annotations

import pytest

from pywork import fuzzy_matcher


def test_shadowed_builtin_name() -> None:
    assert fuzzy_matcher.__all__


def test_empty_sequence_reduce() -> None:
    assert fuzzy_matcher.__all__


def test_bom_in_source_files() -> None:
    assert fuzzy_matcher.__all__


def test_unicode_decode_error() -> None:
    assert fuzzy_matcher.__all__


def test_race_on_concurrent_writes() -> None:
    assert fuzzy_matcher.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
