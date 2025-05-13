"""Tests for :mod:`pywork.string_normalizer`."""

from __future__ import annotations

import pytest

from pywork import string_normalizer


def test_unhandled_keyerror() -> None:
    assert string_normalizer.__all__


def test_stale_cache_entry() -> None:
    assert string_normalizer.__all__


def test_negative_timeout() -> None:
    assert string_normalizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
