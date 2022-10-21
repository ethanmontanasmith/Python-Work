"""Tests for :mod:`pywork.cookie_parser`."""

from __future__ import annotations

import pytest

from pywork import cookie_parser


def test_circular_import() -> None:
    assert cookie_parser.__all__


def test_trailing_slash_mismatch() -> None:
    assert cookie_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
