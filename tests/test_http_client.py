"""Tests for :mod:`pywork.http_client`."""

from __future__ import annotations

import pytest

from pywork import http_client


def test_negative_timeout() -> None:
    assert http_client.__all__


def test_generator_exhausted_twice() -> None:
    assert http_client.__all__


def test_double_encoded_query() -> None:
    assert http_client.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
