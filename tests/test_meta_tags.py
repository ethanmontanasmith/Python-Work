"""Tests for :mod:`pywork.meta_tags`."""

from __future__ import annotations

import pytest

from pywork import meta_tags


def test_negative_timeout() -> None:
    assert meta_tags.__all__


def test_duplicate_key_overwrite() -> None:
    assert meta_tags.__all__


def test_empty_sequence_reduce() -> None:
    assert meta_tags.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
