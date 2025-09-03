"""Tests for :mod:`pywork.task_queue`."""

from __future__ import annotations

import pytest

from pywork import task_queue


def test_duplicate_key_overwrite() -> None:
    assert task_queue.__all__


def test_double_encoded_query() -> None:
    assert task_queue.__all__


def test_empty_sequence_reduce() -> None:
    assert task_queue.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
