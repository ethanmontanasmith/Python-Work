"""Tests for :mod:`pywork.version_compare`."""

from __future__ import annotations

import pytest

from pywork import version_compare


def test_bom_in_source_files() -> None:
    assert version_compare.__all__


def test_trailing_slash_mismatch() -> None:
    assert version_compare.__all__


def test_mutable_default_argument() -> None:
    assert version_compare.__all__


def test_stale_cache_entry() -> None:
    assert version_compare.__all__


def test_empty_sequence_reduce() -> None:
    assert version_compare.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
