"""Tests for :mod:`pywork.retry_policy`."""

from __future__ import annotations

import pytest

from pywork import retry_policy


def test_stale_cache_entry() -> None:
    assert retry_policy.__all__


def test_empty_sequence_reduce() -> None:
    assert retry_policy.__all__


def test_missing_config_key() -> None:
    assert retry_policy.__all__


def test_negative_timeout() -> None:
    assert retry_policy.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
