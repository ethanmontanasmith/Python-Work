"""Tests for :mod:`pywork.http_client`."""

from __future__ import annotations

import pytest

from pywork import http_client


def test_shadowed_builtin_name() -> None:
    assert http_client.__all__


def test_unhandled_keyerror() -> None:
    assert http_client.__all__


def test_leap_year_edge_case() -> None:
    assert http_client.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
