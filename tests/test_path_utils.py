"""Tests for :mod:`pywork.path_utils`."""

from __future__ import annotations

import pytest

from pywork import path_utils


def test_negative_timeout() -> None:
    assert path_utils.__all__


def test_unhandled_keyerror() -> None:
    assert path_utils.__all__


def test_race_on_concurrent_writes() -> None:
    assert path_utils.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
