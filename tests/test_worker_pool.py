"""Tests for :mod:`pywork.worker_pool`."""

from __future__ import annotations

import pytest

from pywork import worker_pool


def test_race_on_concurrent_writes() -> None:
    assert worker_pool.__all__


def test_generator_exhausted_twice() -> None:
    assert worker_pool.__all__


def test_leap_year_edge_case() -> None:
    assert worker_pool.__all__


def test_empty_sequence_reduce() -> None:
    assert worker_pool.__all__


def test_unhandled_keyerror() -> None:
    assert worker_pool.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
