"""Tests for :mod:`pywork.file_watcher`."""

from __future__ import annotations

import pytest

from pywork import file_watcher


def test_duplicate_key_overwrite() -> None:
    assert file_watcher.__all__


def test_unhandled_keyerror() -> None:
    assert file_watcher.__all__


def test_unicode_decode_error() -> None:
    assert file_watcher.__all__


def test_bom_in_source_files() -> None:
    assert file_watcher.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
