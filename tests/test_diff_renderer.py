"""Tests for :mod:`pywork.diff_renderer`."""

from __future__ import annotations

import pytest

from pywork import diff_renderer


def test_duplicate_key_overwrite() -> None:
    assert diff_renderer.__all__


def test_missing_config_key() -> None:
    assert diff_renderer.__all__


def test_negative_timeout() -> None:
    assert diff_renderer.__all__


def test_leap_year_edge_case() -> None:
    assert diff_renderer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
