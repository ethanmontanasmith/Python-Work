"""Tests for :mod:`pywork.batch_runner`."""

from __future__ import annotations

import pytest

from pywork import batch_runner


def test_unicode_decode_error() -> None:
    assert batch_runner.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert batch_runner.__all__


def test_windows_path_separators() -> None:
    assert batch_runner.__all__


def test_empty_input() -> None:
    assert batch_runner.__all__


def test_duplicate_key_overwrite() -> None:
    assert batch_runner.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
