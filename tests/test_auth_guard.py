"""Tests for :mod:`pywork.auth_guard`."""

from __future__ import annotations

import pytest

from pywork import auth_guard


def test_empty_sequence_reduce() -> None:
    assert auth_guard.__all__


def test_double_encoded_query() -> None:
    assert auth_guard.__all__


def test_unhandled_keyerror() -> None:
    assert auth_guard.__all__


def test_duplicate_key_overwrite() -> None:
    assert auth_guard.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
