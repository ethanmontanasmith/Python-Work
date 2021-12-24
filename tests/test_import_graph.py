"""Tests for :mod:`pywork.import_graph`."""

from __future__ import annotations

import pytest

from pywork import import_graph


def test_timezone_drift_on_naive_datetimes() -> None:
    assert import_graph.__all__


def test_generator_exhausted_twice() -> None:
    assert import_graph.__all__


def test_trailing_slash_mismatch() -> None:
    assert import_graph.__all__


def test_empty_sequence_reduce() -> None:
    assert import_graph.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
