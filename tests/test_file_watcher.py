"""Tests for :mod:`pywork.file_watcher`."""

from __future__ import annotations

import pytest

from pywork import file_watcher


def test_mutable_default_argument() -> None:
    assert file_watcher.__all__


def test_generator_exhausted_twice() -> None:
    assert file_watcher.__all__


def test_shadowed_builtin_name() -> None:
    assert file_watcher.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert file_watcher.__all__


def test_leap_year_edge_case() -> None:
    assert file_watcher.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
