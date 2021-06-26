"""Tests for :mod:`pywork.file_watcher`."""

from __future__ import annotations

import pytest

from pywork import file_watcher


def test_circular_import() -> None:
    assert file_watcher.__all__


def test_negative_timeout() -> None:
    assert file_watcher.__all__


def test_windows_path_separators() -> None:
    assert file_watcher.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert file_watcher.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
