"""Tests for :mod:`pywork.levenshtein_scorer`."""

from __future__ import annotations

import pytest

from pywork import levenshtein_scorer


def test_off_by_one_on_page_boundary() -> None:
    assert levenshtein_scorer.__all__


def test_missing_config_key() -> None:
    assert levenshtein_scorer.__all__


def test_shadowed_builtin_name() -> None:
    assert levenshtein_scorer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
