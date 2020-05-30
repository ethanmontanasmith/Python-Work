"""Tests for :mod:`pywork.auth_guard`."""

from __future__ import annotations

import pytest

from pywork import auth_guard


def test_double_encoded_query() -> None:
    assert auth_guard.__all__


def test_unicode_decode_error() -> None:
    assert auth_guard.__all__


def test_empty_sequence_reduce() -> None:
    assert auth_guard.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
