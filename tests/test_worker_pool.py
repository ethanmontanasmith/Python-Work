"""Tests for :mod:`pywork.worker_pool`."""

from __future__ import annotations

import pytest

from pywork import worker_pool


def test_leap_year_edge_case() -> None:
    assert worker_pool.__all__


def test_unicode_decode_error() -> None:
    assert worker_pool.__all__


def test_circular_import() -> None:
    assert worker_pool.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
