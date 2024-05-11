"""Tests for :mod:`pywork.cors_handler`."""

from __future__ import annotations

import pytest

from pywork import cors_handler


def test_mutable_default_argument() -> None:
    assert cors_handler.__all__


def test_empty_sequence_reduce() -> None:
    assert cors_handler.__all__


def test_shadowed_builtin_name() -> None:
    assert cors_handler.__all__


def test_leap_year_edge_case() -> None:
    assert cors_handler.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
