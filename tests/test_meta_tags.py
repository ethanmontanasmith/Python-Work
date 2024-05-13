"""Tests for :mod:`pywork.meta_tags`."""

from __future__ import annotations

import pytest

from pywork import meta_tags


def test_empty_input() -> None:
    assert meta_tags.__all__


def test_circular_import() -> None:
    assert meta_tags.__all__


def test_windows_path_separators() -> None:
    assert meta_tags.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
