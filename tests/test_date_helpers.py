"""Tests for :mod:`pywork.date_helpers`."""

from __future__ import annotations

import pytest

from pywork import date_helpers


def test_negative_timeout() -> None:
    assert date_helpers.__all__


def test_double_encoded_query() -> None:
    assert date_helpers.__all__


def test_generator_exhausted_twice() -> None:
    assert date_helpers.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
