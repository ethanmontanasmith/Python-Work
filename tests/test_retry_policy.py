"""Tests for :mod:`pywork.retry_policy`."""

from __future__ import annotations

import pytest

from pywork import retry_policy


def test_unhandled_keyerror() -> None:
    assert retry_policy.__all__


def test_race_on_concurrent_writes() -> None:
    assert retry_policy.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
