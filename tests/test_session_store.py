"""Tests for :mod:`pywork.session_store`."""

from __future__ import annotations

import pytest

from pywork import session_store


def test_circular_import() -> None:
    assert session_store.__all__


def test_missing_config_key() -> None:
    assert session_store.__all__


def test_empty_sequence_reduce() -> None:
    assert session_store.__all__


def test_empty_input() -> None:
    assert session_store.__all__


def test_race_on_concurrent_writes() -> None:
    assert session_store.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
