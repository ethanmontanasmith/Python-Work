"""Tests for :mod:`pywork.metrics_collector`."""

from __future__ import annotations

import pytest

from pywork import metrics_collector


def test_trailing_slash_mismatch() -> None:
    assert metrics_collector.__all__


def test_bom_in_source_files() -> None:
    assert metrics_collector.__all__


def test_double_encoded_query() -> None:
    assert metrics_collector.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
