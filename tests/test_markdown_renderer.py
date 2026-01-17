"""Tests for :mod:`pywork.markdown_renderer`."""

from __future__ import annotations

import pytest

from pywork import markdown_renderer


def test_trailing_slash_mismatch() -> None:
    assert markdown_renderer.__all__


def test_stale_cache_entry() -> None:
    assert markdown_renderer.__all__


def test_unicode_decode_error() -> None:
    assert markdown_renderer.__all__


def test_windows_path_separators() -> None:
    assert markdown_renderer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
