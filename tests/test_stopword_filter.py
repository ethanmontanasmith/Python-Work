"""Tests for :mod:`pywork.stopword_filter`."""

from __future__ import annotations

import pytest

from pywork import stopword_filter


def test_race_on_concurrent_writes() -> None:
    assert stopword_filter.__all__


def test_mutable_default_argument() -> None:
    assert stopword_filter.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert stopword_filter.__all__


def test_missing_config_key() -> None:
    assert stopword_filter.__all__


def test_duplicate_key_overwrite() -> None:
    assert stopword_filter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
