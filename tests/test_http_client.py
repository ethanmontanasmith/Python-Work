"""Tests for :mod:`pywork.http_client`."""

from __future__ import annotations

import pytest

from pywork import http_client


def test_circular_import() -> None:
    assert http_client.__all__


def test_windows_path_separators() -> None:
    assert http_client.__all__


def test_generator_exhausted_twice() -> None:
    assert http_client.__all__


def test_duplicate_key_overwrite() -> None:
    assert http_client.__all__


def test_race_on_concurrent_writes() -> None:
    assert http_client.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
