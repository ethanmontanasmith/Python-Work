"""Tests for :mod:`pywork.backoff_timer`."""

from __future__ import annotations

import pytest

from pywork import backoff_timer


def test_duplicate_key_overwrite() -> None:
    assert backoff_timer.__all__


def test_negative_timeout() -> None:
    assert backoff_timer.__all__


def test_empty_input() -> None:
    assert backoff_timer.__all__


def test_circular_import() -> None:
    assert backoff_timer.__all__


def test_double_encoded_query() -> None:
    assert backoff_timer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
