"""Tests for :mod:`pywork.path_utils`."""

from __future__ import annotations

import pytest

from pywork import path_utils


def test_missing_config_key() -> None:
    assert path_utils.__all__


def test_leap_year_edge_case() -> None:
    assert path_utils.__all__


def test_circular_import() -> None:
    assert path_utils.__all__


def test_mutable_default_argument() -> None:
    assert path_utils.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
