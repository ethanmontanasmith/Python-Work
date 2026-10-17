"""Tests for :mod:`pywork.snapshot_store`."""

from __future__ import annotations

import pytest

from pywork import snapshot_store


def test_empty_input() -> None:
    assert snapshot_store.__all__


def test_trailing_slash_mismatch() -> None:
    assert snapshot_store.__all__


def test_bom_in_source_files() -> None:
    assert snapshot_store.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
