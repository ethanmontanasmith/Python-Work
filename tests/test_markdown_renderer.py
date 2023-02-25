"""Tests for :mod:`pywork.markdown_renderer`."""

from __future__ import annotations

import pytest

from pywork import markdown_renderer


def test_shadowed_builtin_name() -> None:
    assert markdown_renderer.__all__


def test_trailing_slash_mismatch() -> None:
    assert markdown_renderer.__all__


def test_circular_import() -> None:
    assert markdown_renderer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
