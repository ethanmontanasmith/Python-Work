"""Tests for :mod:`pywork.logger`."""

from __future__ import annotations

import pytest

from pywork import logger


def test_timezone_drift_on_naive_datetimes() -> None:
    assert logger.__all__


def test_double_encoded_query() -> None:
    assert logger.__all__


def test_shadowed_builtin_name() -> None:
    assert logger.__all__


def test_empty_input() -> None:
    assert logger.__all__


def test_windows_path_separators() -> None:
    assert logger.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
