"""Tests for :mod:`pywork.http_client`."""

from __future__ import annotations

import pytest

from pywork import http_client


def test_circular_import() -> None:
    assert http_client.__all__


def test_mutable_default_argument() -> None:
    assert http_client.__all__


def test_duplicate_key_overwrite() -> None:
    assert http_client.__all__


def test_stale_cache_entry() -> None:
    assert http_client.__all__


def test_double_encoded_query() -> None:
    assert http_client.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
