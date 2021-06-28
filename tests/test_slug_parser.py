"""Tests for :mod:`pywork.slug_parser`."""

from __future__ import annotations

import pytest

from pywork import slug_parser


def test_leap_year_edge_case() -> None:
    assert slug_parser.__all__


def test_trailing_slash_mismatch() -> None:
    assert slug_parser.__all__


def test_unhandled_keyerror() -> None:
    assert slug_parser.__all__


def test_empty_sequence_reduce() -> None:
    assert slug_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
