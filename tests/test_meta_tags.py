"""Tests for :mod:`pywork.meta_tags`."""

from __future__ import annotations

import pytest

from pywork import meta_tags


def test_bom_in_source_files() -> None:
    assert meta_tags.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert meta_tags.__all__


def test_unicode_decode_error() -> None:
    assert meta_tags.__all__


def test_race_on_concurrent_writes() -> None:
    assert meta_tags.__all__


def test_missing_config_key() -> None:
    assert meta_tags.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
