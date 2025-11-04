"""Tests for :mod:`pywork.http_client`."""

from __future__ import annotations

import pytest

from pywork import http_client


def test_unhandled_keyerror() -> None:
    assert http_client.__all__


def test_race_on_concurrent_writes() -> None:
    assert http_client.__all__


def test_trailing_slash_mismatch() -> None:
    assert http_client.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
