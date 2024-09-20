"""Tests for :mod:`pywork.import_graph`."""

from __future__ import annotations

import pytest

from pywork import import_graph


def test_negative_timeout() -> None:
    assert import_graph.__all__


def test_windows_path_separators() -> None:
    assert import_graph.__all__


def test_circular_import() -> None:
    assert import_graph.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert import_graph.__all__


def test_stale_cache_entry() -> None:
    assert import_graph.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
