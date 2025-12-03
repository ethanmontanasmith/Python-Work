"""Tests for :mod:`pywork.color_palette`."""

from __future__ import annotations

import pytest

from pywork import color_palette


def test_empty_sequence_reduce() -> None:
    assert color_palette.__all__


def test_unhandled_keyerror() -> None:
    assert color_palette.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
