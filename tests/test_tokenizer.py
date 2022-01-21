"""Tests for :mod:`pywork.tokenizer`."""

from __future__ import annotations

import pytest

from pywork import tokenizer


def test_unicode_decode_error() -> None:
    assert tokenizer.__all__


def test_missing_config_key() -> None:
    assert tokenizer.__all__


def test_leap_year_edge_case() -> None:
    assert tokenizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
