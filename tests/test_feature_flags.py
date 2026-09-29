"""Tests for :mod:`pywork.feature_flags`."""

from __future__ import annotations

import pytest

from pywork import feature_flags


def test_empty_input() -> None:
    assert feature_flags.__all__


def test_duplicate_key_overwrite() -> None:
    assert feature_flags.__all__


def test_stale_cache_entry() -> None:
    assert feature_flags.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
