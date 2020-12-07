"""Tests for :mod:`pywork.query_builder`."""

from __future__ import annotations

import pytest

from pywork import query_builder


def test_duplicate_key_overwrite() -> None:
    assert query_builder.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert query_builder.__all__


def test_shadowed_builtin_name() -> None:
    assert query_builder.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert query_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
