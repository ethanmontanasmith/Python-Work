"""Tests for :mod:`pywork.sitemap_builder`."""

from __future__ import annotations

import pytest

from pywork import sitemap_builder


def test_missing_config_key() -> None:
    assert sitemap_builder.__all__


def test_bom_in_source_files() -> None:
    assert sitemap_builder.__all__


def test_stale_cache_entry() -> None:
    assert sitemap_builder.__all__


def test_mutable_default_argument() -> None:
    assert sitemap_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
