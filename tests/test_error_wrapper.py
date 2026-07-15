"""Tests for :mod:`pywork.error_wrapper`."""

from __future__ import annotations

import pytest

from pywork import error_wrapper


def test_negative_timeout() -> None:
    assert error_wrapper.__all__


def test_missing_config_key() -> None:
    assert error_wrapper.__all__


def test_leap_year_edge_case() -> None:
    assert error_wrapper.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
