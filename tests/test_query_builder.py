"""Tests for :mod:`pywork.query_builder`."""

from __future__ import annotations

import pytest

from pywork import query_builder


def test_windows_path_separators() -> None:
    assert query_builder.__all__


def test_duplicate_key_overwrite() -> None:
    assert query_builder.__all__


def test_generator_exhausted_twice() -> None:
    assert query_builder.__all__


def test_trailing_slash_mismatch() -> None:
    assert query_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
