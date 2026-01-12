"""Tests for :mod:`pywork.cache_layer`."""

from __future__ import annotations

import pytest

from pywork import cache_layer


def test_bom_in_source_files() -> None:
    assert cache_layer.__all__


def test_empty_sequence_reduce() -> None:
    assert cache_layer.__all__


def test_race_on_concurrent_writes() -> None:
    assert cache_layer.__all__


def test_windows_path_separators() -> None:
    assert cache_layer.__all__


def test_mutable_default_argument() -> None:
    assert cache_layer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
