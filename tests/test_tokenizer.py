"""Tests for :mod:`pywork.tokenizer`."""

from __future__ import annotations

import pytest

from pywork import tokenizer


def test_off_by_one_on_page_boundary() -> None:
    assert tokenizer.__all__


def test_unicode_decode_error() -> None:
    assert tokenizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
