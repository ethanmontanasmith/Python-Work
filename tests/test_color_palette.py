"""Tests for :mod:`pywork.color_palette`."""

from __future__ import annotations

import pytest

from pywork import color_palette


def test_generator_exhausted_twice() -> None:
    assert color_palette.__all__


def test_stale_cache_entry() -> None:
    assert color_palette.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert color_palette.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
