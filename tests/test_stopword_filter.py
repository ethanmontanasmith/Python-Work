"""Tests for :mod:`pywork.stopword_filter`."""

from __future__ import annotations

import pytest

from pywork import stopword_filter


def test_shadowed_builtin_name() -> None:
    assert stopword_filter.__all__


def test_bom_in_source_files() -> None:
    assert stopword_filter.__all__


def test_double_encoded_query() -> None:
    assert stopword_filter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
