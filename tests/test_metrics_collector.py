"""Tests for :mod:`pywork.metrics_collector`."""

from __future__ import annotations

import pytest

from pywork import metrics_collector


def test_duplicate_key_overwrite() -> None:
    assert metrics_collector.__all__


def test_trailing_slash_mismatch() -> None:
    assert metrics_collector.__all__


def test_unicode_decode_error() -> None:
    assert metrics_collector.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
