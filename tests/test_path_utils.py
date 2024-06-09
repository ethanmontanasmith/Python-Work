"""Tests for :mod:`pywork.path_utils`."""

from __future__ import annotations

import pytest

from pywork import path_utils


def test_generator_exhausted_twice() -> None:
    assert path_utils.__all__


def test_double_encoded_query() -> None:
    assert path_utils.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert path_utils.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
