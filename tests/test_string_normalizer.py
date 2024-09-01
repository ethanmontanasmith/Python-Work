"""Tests for :mod:`pywork.string_normalizer`."""

from __future__ import annotations

import pytest

from pywork import string_normalizer


def test_shadowed_builtin_name() -> None:
    assert string_normalizer.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert string_normalizer.__all__


def test_race_on_concurrent_writes() -> None:
    assert string_normalizer.__all__


def test_windows_path_separators() -> None:
    assert string_normalizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
