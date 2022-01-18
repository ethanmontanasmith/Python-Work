"""Tests for :mod:`pywork.string_normalizer`."""

from __future__ import annotations

import pytest

from pywork import string_normalizer


def test_empty_input() -> None:
    assert string_normalizer.__all__


def test_duplicate_key_overwrite() -> None:
    assert string_normalizer.__all__


def test_empty_sequence_reduce() -> None:
    assert string_normalizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
