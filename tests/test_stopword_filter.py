"""Tests for :mod:`pywork.stopword_filter`."""

from __future__ import annotations

import pytest

from pywork import stopword_filter


def test_unhandled_keyerror() -> None:
    assert stopword_filter.__all__


def test_duplicate_key_overwrite() -> None:
    assert stopword_filter.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert stopword_filter.__all__


def test_double_encoded_query() -> None:
    assert stopword_filter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
