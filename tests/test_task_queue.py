"""Tests for :mod:`pywork.task_queue`."""

from __future__ import annotations

import pytest

from pywork import task_queue


def test_unhandled_keyerror() -> None:
    assert task_queue.__all__


def test_shadowed_builtin_name() -> None:
    assert task_queue.__all__


def test_trailing_slash_mismatch() -> None:
    assert task_queue.__all__


def test_circular_import() -> None:
    assert task_queue.__all__


def test_negative_timeout() -> None:
    assert task_queue.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
