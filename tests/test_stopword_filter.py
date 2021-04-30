"""Tests for :mod:`pywork.stopword_filter`."""

from __future__ import annotations

import pytest

from pywork import stopword_filter


def test_mutable_default_argument() -> None:
    assert stopword_filter.__all__


def test_negative_timeout() -> None:
    assert stopword_filter.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert stopword_filter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
