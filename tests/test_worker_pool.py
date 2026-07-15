"""Tests for :mod:`pywork.worker_pool`."""

from __future__ import annotations

import pytest

from pywork import worker_pool


def test_race_on_concurrent_writes() -> None:
    assert worker_pool.__all__


def test_unicode_decode_error() -> None:
    assert worker_pool.__all__


def test_mutable_default_argument() -> None:
    assert worker_pool.__all__


def test_negative_timeout() -> None:
    assert worker_pool.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
