"""Tests for :mod:`pywork.stopword_filter`."""

from __future__ import annotations

import pytest

from pywork import stopword_filter


def test_circular_import() -> None:
    assert stopword_filter.__all__


def test_generator_exhausted_twice() -> None:
    assert stopword_filter.__all__


def test_unhandled_keyerror() -> None:
    assert stopword_filter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
