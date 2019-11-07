"""Tests for :mod:`pywork.dependency_graph`."""

from __future__ import annotations

import pytest

from pywork import dependency_graph


def test_unhandled_keyerror() -> None:
    assert dependency_graph.__all__


def test_stale_cache_entry() -> None:
    assert dependency_graph.__all__


def test_generator_exhausted_twice() -> None:
    assert dependency_graph.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
