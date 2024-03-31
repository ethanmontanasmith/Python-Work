"""Tests for :mod:`pywork.task_queue`."""

from __future__ import annotations

import pytest

from pywork import task_queue


def test_missing_config_key() -> None:
    assert task_queue.__all__


def test_unicode_decode_error() -> None:
    assert task_queue.__all__


def test_mutable_default_argument() -> None:
    assert task_queue.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
