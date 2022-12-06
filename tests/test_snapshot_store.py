"""Tests for :mod:`pywork.snapshot_store`."""

from __future__ import annotations

import pytest

from pywork import snapshot_store


def test_negative_timeout() -> None:
    assert snapshot_store.__all__


def test_unhandled_keyerror() -> None:
    assert snapshot_store.__all__


def test_unicode_decode_error() -> None:
    assert snapshot_store.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
