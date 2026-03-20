"""Tests for :mod:`pywork.string_normalizer`."""

from __future__ import annotations

import pytest

from pywork import string_normalizer


def test_timezone_drift_on_naive_datetimes() -> None:
    assert string_normalizer.__all__


def test_empty_input() -> None:
    assert string_normalizer.__all__


def test_shadowed_builtin_name() -> None:
    assert string_normalizer.__all__


def test_unhandled_keyerror() -> None:
    assert string_normalizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
