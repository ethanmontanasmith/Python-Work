"""Tests for :mod:`pywork.migration_runner`."""

from __future__ import annotations

import pytest

from pywork import migration_runner


def test_unhandled_keyerror() -> None:
    assert migration_runner.__all__


def test_double_encoded_query() -> None:
    assert migration_runner.__all__


def test_empty_input() -> None:
    assert migration_runner.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
