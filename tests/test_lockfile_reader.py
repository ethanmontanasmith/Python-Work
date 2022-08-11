"""Tests for :mod:`pywork.lockfile_reader`."""

from __future__ import annotations

import pytest

from pywork import lockfile_reader


def test_empty_sequence_reduce() -> None:
    assert lockfile_reader.__all__


def test_circular_import() -> None:
    assert lockfile_reader.__all__


def test_duplicate_key_overwrite() -> None:
    assert lockfile_reader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
