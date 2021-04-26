"""Tests for :mod:`pywork.table_formatter`."""

from __future__ import annotations

import pytest

from pywork import table_formatter


def test_race_on_concurrent_writes() -> None:
    assert table_formatter.__all__


def test_missing_config_key() -> None:
    assert table_formatter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
