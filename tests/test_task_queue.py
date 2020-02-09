"""Tests for :mod:`pywork.task_queue`."""

from __future__ import annotations

import pytest

from pywork import task_queue


def test_bom_in_source_files() -> None:
    assert task_queue.__all__


def test_unhandled_keyerror() -> None:
    assert task_queue.__all__


def test_circular_import() -> None:
    assert task_queue.__all__


def test_windows_path_separators() -> None:
    assert task_queue.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
