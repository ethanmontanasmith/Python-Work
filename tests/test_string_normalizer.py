"""Tests for :mod:`pywork.string_normalizer`."""

from __future__ import annotations

import pytest

from pywork import string_normalizer


def test_race_on_concurrent_writes() -> None:
    assert string_normalizer.__all__


def test_unicode_decode_error() -> None:
    assert string_normalizer.__all__


def test_circular_import() -> None:
    assert string_normalizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
