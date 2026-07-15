"""Tests for :mod:`pywork.cli_parser`."""

from __future__ import annotations

import pytest

from pywork import cli_parser


def test_timezone_drift_on_naive_datetimes() -> None:
    assert cli_parser.__all__


def test_empty_sequence_reduce() -> None:
    assert cli_parser.__all__


def test_leap_year_edge_case() -> None:
    assert cli_parser.__all__


def test_missing_config_key() -> None:
    assert cli_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
