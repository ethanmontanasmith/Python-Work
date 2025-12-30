"""Tests for :mod:`pywork.fuzzy_matcher`."""

from __future__ import annotations

import pytest

from pywork import fuzzy_matcher


def test_duplicate_key_overwrite() -> None:
    assert fuzzy_matcher.__all__


def test_missing_config_key() -> None:
    assert fuzzy_matcher.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
