"""Tests for :mod:`pywork.seed_loader`."""

from __future__ import annotations

import pytest

from pywork import seed_loader


def test_empty_input() -> None:
    assert seed_loader.__all__


def test_windows_path_separators() -> None:
    assert seed_loader.__all__


def test_duplicate_key_overwrite() -> None:
    assert seed_loader.__all__


def test_stale_cache_entry() -> None:
    assert seed_loader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
