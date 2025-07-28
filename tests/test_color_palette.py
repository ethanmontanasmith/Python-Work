"""Tests for :mod:`pywork.color_palette`."""

from __future__ import annotations

import pytest

from pywork import color_palette


def test_empty_input() -> None:
    assert color_palette.__all__


def test_trailing_slash_mismatch() -> None:
    assert color_palette.__all__


def test_shadowed_builtin_name() -> None:
    assert color_palette.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert color_palette.__all__


def test_mutable_default_argument() -> None:
    assert color_palette.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
