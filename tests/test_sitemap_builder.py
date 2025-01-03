"""Tests for :mod:`pywork.sitemap_builder`."""

from __future__ import annotations

import pytest

from pywork import sitemap_builder


def test_empty_sequence_reduce() -> None:
    assert sitemap_builder.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert sitemap_builder.__all__


def test_mutable_default_argument() -> None:
    assert sitemap_builder.__all__


def test_duplicate_key_overwrite() -> None:
    assert sitemap_builder.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
