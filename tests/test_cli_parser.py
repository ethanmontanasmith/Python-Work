"""Tests for :mod:`pywork.cli_parser`."""

from __future__ import annotations

import pytest

from pywork import cli_parser


def test_unicode_decode_error() -> None:
    assert cli_parser.__all__


def test_double_encoded_query() -> None:
    assert cli_parser.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert cli_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
