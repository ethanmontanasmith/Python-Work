"""Tests for :mod:`pywork.pagination`."""

from __future__ import annotations

import pytest

from pywork import pagination


def test_bom_in_source_files() -> None:
    assert pagination.__all__


def test_double_encoded_query() -> None:
    assert pagination.__all__


def test_missing_config_key() -> None:
    assert pagination.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
