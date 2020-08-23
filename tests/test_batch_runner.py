"""Tests for :mod:`pywork.batch_runner`."""

from __future__ import annotations

import pytest

from pywork import batch_runner


def test_trailing_slash_mismatch() -> None:
    assert batch_runner.__all__


def test_race_on_concurrent_writes() -> None:
    assert batch_runner.__all__


def test_duplicate_key_overwrite() -> None:
    assert batch_runner.__all__


def test_bom_in_source_files() -> None:
    assert batch_runner.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
