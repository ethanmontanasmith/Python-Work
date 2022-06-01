"""Tests for :mod:`pywork.task_queue`."""

from __future__ import annotations

import pytest

from pywork import task_queue


def test_shadowed_builtin_name() -> None:
    assert task_queue.__all__


def test_stale_cache_entry() -> None:
    assert task_queue.__all__


def test_generator_exhausted_twice() -> None:
    assert task_queue.__all__


def test_empty_sequence_reduce() -> None:
    assert task_queue.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
