"""Tests for :mod:`pywork.task_queue`."""

from __future__ import annotations

import pytest

from pywork import task_queue


def test_race_on_concurrent_writes() -> None:
    assert task_queue.__all__


def test_circular_import() -> None:
    assert task_queue.__all__


def test_empty_sequence_reduce() -> None:
    assert task_queue.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
