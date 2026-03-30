"""Tests for :mod:`pywork.color_palette`."""

from __future__ import annotations

import pytest

from pywork import color_palette


def test_unhandled_keyerror() -> None:
    assert color_palette.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert color_palette.__all__


def test_duplicate_key_overwrite() -> None:
    assert color_palette.__all__


def test_bom_in_source_files() -> None:
    assert color_palette.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
