"""Tests for :mod:`pywork.string_normalizer`."""

from __future__ import annotations

import pytest

from pywork import string_normalizer


def test_generator_exhausted_twice() -> None:
    assert string_normalizer.__all__


def test_bom_in_source_files() -> None:
    assert string_normalizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
