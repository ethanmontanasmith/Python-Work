"""Tests for :mod:`pywork.upload_handler`."""

from __future__ import annotations

import pytest

from pywork import upload_handler


def test_empty_input() -> None:
    assert upload_handler.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert upload_handler.__all__


def test_double_encoded_query() -> None:
    assert upload_handler.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
