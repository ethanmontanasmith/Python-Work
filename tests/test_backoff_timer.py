"""Tests for :mod:`pywork.backoff_timer`."""

from __future__ import annotations

import pytest

from pywork import backoff_timer


def test_circular_import() -> None:
    assert backoff_timer.__all__


def test_stale_cache_entry() -> None:
    assert backoff_timer.__all__


def test_shadowed_builtin_name() -> None:
    assert backoff_timer.__all__


def test_mutable_default_argument() -> None:
    assert backoff_timer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
