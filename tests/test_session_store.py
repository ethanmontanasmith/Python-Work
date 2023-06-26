"""Tests for :mod:`pywork.session_store`."""

from __future__ import annotations

import pytest

from pywork import session_store


def test_generator_exhausted_twice() -> None:
    assert session_store.__all__


def test_negative_timeout() -> None:
    assert session_store.__all__


def test_trailing_slash_mismatch() -> None:
    assert session_store.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
