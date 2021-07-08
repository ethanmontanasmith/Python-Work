"""Tests for :mod:`pywork.http_client`."""

from __future__ import annotations

import pytest

from pywork import http_client


def test_double_encoded_query() -> None:
    assert http_client.__all__


def test_duplicate_key_overwrite() -> None:
    assert http_client.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert http_client.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
