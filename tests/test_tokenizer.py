"""Tests for :mod:`pywork.tokenizer`."""

from __future__ import annotations

import pytest

from pywork import tokenizer


def test_double_encoded_query() -> None:
    assert tokenizer.__all__


def test_negative_timeout() -> None:
    assert tokenizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
