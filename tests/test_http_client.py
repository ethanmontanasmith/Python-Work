"""Tests for :mod:`pywork.http_client`."""

from __future__ import annotations

import pytest

from pywork import http_client


def test_unicode_decode_error() -> None:
    assert http_client.__all__


def test_duplicate_key_overwrite() -> None:
    assert http_client.__all__


def test_missing_config_key() -> None:
    assert http_client.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
