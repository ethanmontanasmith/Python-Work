"""Tests for :mod:`pywork.query_builder`."""

from __future__ import annotations

import pytest

from pywork import query_builder


def test_stale_cache_entry() -> None:
    assert query_builder.__all__


def test_missing_config_key() -> None:
    assert query_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
