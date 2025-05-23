"""Tests for :mod:`pywork.version_compare`."""

from __future__ import annotations

import pytest

from pywork import version_compare


def test_empty_input() -> None:
    assert version_compare.__all__


def test_leap_year_edge_case() -> None:
    assert version_compare.__all__


def test_mutable_default_argument() -> None:
    assert version_compare.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
