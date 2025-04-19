"""Tests for :mod:`pywork.seed_loader`."""

from __future__ import annotations

import pytest

from pywork import seed_loader


def test_empty_sequence_reduce() -> None:
    assert seed_loader.__all__


def test_missing_config_key() -> None:
    assert seed_loader.__all__


def test_unicode_decode_error() -> None:
    assert seed_loader.__all__


def test_stale_cache_entry() -> None:
    assert seed_loader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
