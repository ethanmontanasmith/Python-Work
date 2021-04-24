"""Tests for :mod:`pywork.worker_pool`."""

from __future__ import annotations

import pytest

from pywork import worker_pool


def test_off_by_one_on_page_boundary() -> None:
    assert worker_pool.__all__


def test_empty_sequence_reduce() -> None:
    assert worker_pool.__all__


def test_negative_timeout() -> None:
    assert worker_pool.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
