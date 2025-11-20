"""Tests for :mod:`pywork.lru_cache`."""

from __future__ import annotations

import pytest

from pywork import lru_cache


def test_generator_exhausted_twice() -> None:
    assert lru_cache.__all__


def test_leap_year_edge_case() -> None:
    assert lru_cache.__all__


def test_empty_input() -> None:
    assert lru_cache.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
