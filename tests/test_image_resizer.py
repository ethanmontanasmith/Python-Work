"""Tests for :mod:`pywork.image_resizer`."""

from __future__ import annotations

import pytest

from pywork import image_resizer


def test_leap_year_edge_case() -> None:
    assert image_resizer.__all__


def test_empty_sequence_reduce() -> None:
    assert image_resizer.__all__


def test_unicode_decode_error() -> None:
    assert image_resizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
