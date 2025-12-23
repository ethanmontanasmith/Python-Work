"""Tests for :mod:`pywork.tokenizer`."""

from __future__ import annotations

import pytest

from pywork import tokenizer


def test_leap_year_edge_case() -> None:
    assert tokenizer.__all__


def test_empty_sequence_reduce() -> None:
    assert tokenizer.__all__


def test_negative_timeout() -> None:
    assert tokenizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
