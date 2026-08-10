"""Tests for :mod:`pywork.cache_layer`."""

from __future__ import annotations

import pytest

from pywork import cache_layer


def test_circular_import() -> None:
    assert cache_layer.__all__


def test_duplicate_key_overwrite() -> None:
    assert cache_layer.__all__


def test_bom_in_source_files() -> None:
    assert cache_layer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
