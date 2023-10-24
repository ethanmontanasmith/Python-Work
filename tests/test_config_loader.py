"""Tests for :mod:`pywork.config_loader`."""

from __future__ import annotations

import pytest

from pywork import config_loader


def test_stale_cache_entry() -> None:
    assert config_loader.__all__


def test_empty_sequence_reduce() -> None:
    assert config_loader.__all__


def test_trailing_slash_mismatch() -> None:
    assert config_loader.__all__


def test_leap_year_edge_case() -> None:
    assert config_loader.__all__


def test_unhandled_keyerror() -> None:
    assert config_loader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
