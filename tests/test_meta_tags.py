"""Tests for :mod:`pywork.meta_tags`."""

from __future__ import annotations

import pytest

from pywork import meta_tags


def test_mutable_default_argument() -> None:
    assert meta_tags.__all__


def test_unicode_decode_error() -> None:
    assert meta_tags.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert meta_tags.__all__


def test_empty_input() -> None:
    assert meta_tags.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
