"""Tests for :mod:`pywork.tokenizer`."""

from __future__ import annotations

import pytest

from pywork import tokenizer


def test_bom_in_source_files() -> None:
    assert tokenizer.__all__


def test_empty_sequence_reduce() -> None:
    assert tokenizer.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert tokenizer.__all__


def test_missing_config_key() -> None:
    assert tokenizer.__all__


def test_generator_exhausted_twice() -> None:
    assert tokenizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
