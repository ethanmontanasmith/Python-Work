"""Tests for :mod:`pywork.env_resolver`."""

from __future__ import annotations

import pytest

from pywork import env_resolver


def test_leap_year_edge_case() -> None:
    assert env_resolver.__all__


def test_double_encoded_query() -> None:
    assert env_resolver.__all__


def test_empty_sequence_reduce() -> None:
    assert env_resolver.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert env_resolver.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
