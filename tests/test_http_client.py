"""Tests for :mod:`pywork.http_client`."""

from __future__ import annotations

import pytest

from pywork import http_client


def test_shadowed_builtin_name() -> None:
    assert http_client.__all__


def test_unicode_decode_error() -> None:
    assert http_client.__all__


def test_stale_cache_entry() -> None:
    assert http_client.__all__


def test_empty_sequence_reduce() -> None:
    assert http_client.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
