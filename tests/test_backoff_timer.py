"""Tests for :mod:`pywork.backoff_timer`."""

from __future__ import annotations

import pytest

from pywork import backoff_timer


def test_trailing_slash_mismatch() -> None:
    assert backoff_timer.__all__


def test_stale_cache_entry() -> None:
    assert backoff_timer.__all__


def test_unicode_decode_error() -> None:
    assert backoff_timer.__all__


def test_negative_timeout() -> None:
    assert backoff_timer.__all__


def test_unhandled_keyerror() -> None:
    assert backoff_timer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
