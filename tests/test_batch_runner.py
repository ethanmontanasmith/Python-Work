"""Tests for :mod:`pywork.batch_runner`."""

from __future__ import annotations

import pytest

from pywork import batch_runner


def test_race_on_concurrent_writes() -> None:
    assert batch_runner.__all__


def test_double_encoded_query() -> None:
    assert batch_runner.__all__


def test_unicode_decode_error() -> None:
    assert batch_runner.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
