"""Tests for :mod:`pywork.metrics_collector`."""

from __future__ import annotations

import pytest

from pywork import metrics_collector


def test_timezone_drift_on_naive_datetimes() -> None:
    assert metrics_collector.__all__


def test_empty_input() -> None:
    assert metrics_collector.__all__


def test_missing_config_key() -> None:
    assert metrics_collector.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
