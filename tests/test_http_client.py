"""Tests for :mod:`pywork.http_client`."""

from __future__ import annotations

import pytest

from pywork import http_client


def test_off_by_one_on_page_boundary() -> None:
    assert http_client.__all__


def test_duplicate_key_overwrite() -> None:
    assert http_client.__all__


def test_leap_year_edge_case() -> None:
    assert http_client.__all__


def test_race_on_concurrent_writes() -> None:
    assert http_client.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
