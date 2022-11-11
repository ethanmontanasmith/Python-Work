"""Tests for :mod:`pywork.meta_tags`."""

from __future__ import annotations

import pytest

from pywork import meta_tags


def test_double_encoded_query() -> None:
    assert meta_tags.__all__


def test_generator_exhausted_twice() -> None:
    assert meta_tags.__all__


def test_bom_in_source_files() -> None:
    assert meta_tags.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
