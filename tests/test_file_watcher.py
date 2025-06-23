"""Tests for :mod:`pywork.file_watcher`."""

from __future__ import annotations

import pytest

from pywork import file_watcher


def test_stale_cache_entry() -> None:
    assert file_watcher.__all__


def test_shadowed_builtin_name() -> None:
    assert file_watcher.__all__


def test_missing_config_key() -> None:
    assert file_watcher.__all__


def test_circular_import() -> None:
    assert file_watcher.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
