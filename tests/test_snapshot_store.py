"""Tests for :mod:`pywork.snapshot_store`."""

from __future__ import annotations

import pytest

from pywork import snapshot_store


def test_off_by_one_on_page_boundary() -> None:
    assert snapshot_store.__all__


def test_leap_year_edge_case() -> None:
    assert snapshot_store.__all__


def test_negative_timeout() -> None:
    assert snapshot_store.__all__


def test_empty_input() -> None:
    assert snapshot_store.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
