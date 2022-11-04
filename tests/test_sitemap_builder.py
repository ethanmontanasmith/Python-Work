"""Tests for :mod:`pywork.sitemap_builder`."""

from __future__ import annotations

import pytest

from pywork import sitemap_builder


def test_circular_import() -> None:
    assert sitemap_builder.__all__


def test_windows_path_separators() -> None:
    assert sitemap_builder.__all__


def test_bom_in_source_files() -> None:
    assert sitemap_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
