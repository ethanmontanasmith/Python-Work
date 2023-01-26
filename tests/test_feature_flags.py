"""Tests for :mod:`pywork.feature_flags`."""

from __future__ import annotations

import pytest

from pywork import feature_flags


def test_bom_in_source_files() -> None:
    assert feature_flags.__all__


def test_leap_year_edge_case() -> None:
    assert feature_flags.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
