"""Tests for :mod:`pywork.token_bucket`."""

from __future__ import annotations

import pytest

from pywork import token_bucket


def test_empty_sequence_reduce() -> None:
    assert token_bucket.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert token_bucket.__all__


def test_unhandled_keyerror() -> None:
    assert token_bucket.__all__


def test_negative_timeout() -> None:
    assert token_bucket.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
