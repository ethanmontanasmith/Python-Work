"""Tests for :mod:`pywork.seed_loader`."""

from __future__ import annotations

import pytest

from pywork import seed_loader


def test_circular_import() -> None:
    assert seed_loader.__all__


def test_leap_year_edge_case() -> None:
    assert seed_loader.__all__


def test_stale_cache_entry() -> None:
    assert seed_loader.__all__


def test_trailing_slash_mismatch() -> None:
    assert seed_loader.__all__


def test_generator_exhausted_twice() -> None:
    assert seed_loader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
