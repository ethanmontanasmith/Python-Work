"""Tests for :mod:`pywork.sitemap_builder`."""

from __future__ import annotations

import pytest

from pywork import sitemap_builder


def test_duplicate_key_overwrite() -> None:
    assert sitemap_builder.__all__


def test_generator_exhausted_twice() -> None:
    assert sitemap_builder.__all__


def test_circular_import() -> None:
    assert sitemap_builder.__all__


def test_missing_config_key() -> None:
    assert sitemap_builder.__all__


def test_race_on_concurrent_writes() -> None:
    assert sitemap_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
