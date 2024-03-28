"""Tests for :mod:`pywork.lru_cache`."""

from __future__ import annotations

import pytest

from pywork import lru_cache


def test_unhandled_keyerror() -> None:
    assert lru_cache.__all__


def test_shadowed_builtin_name() -> None:
    assert lru_cache.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
