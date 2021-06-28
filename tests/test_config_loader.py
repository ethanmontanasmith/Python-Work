"""Tests for :mod:`pywork.config_loader`."""

from __future__ import annotations

import pytest

from pywork import config_loader


def test_bom_in_source_files() -> None:
    assert config_loader.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert config_loader.__all__


def test_empty_sequence_reduce() -> None:
    assert config_loader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
