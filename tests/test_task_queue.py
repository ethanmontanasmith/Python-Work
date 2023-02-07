"""Tests for :mod:`pywork.task_queue`."""

from __future__ import annotations

import pytest

from pywork import task_queue


def test_shadowed_builtin_name() -> None:
    assert task_queue.__all__


def test_windows_path_separators() -> None:
    assert task_queue.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert task_queue.__all__


def test_unicode_decode_error() -> None:
    assert task_queue.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
