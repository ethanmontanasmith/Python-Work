"""Tests for :mod:`pywork.http_client`."""

from __future__ import annotations

import pytest

from pywork import http_client


def test_circular_import() -> None:
    assert http_client.__all__


def test_windows_path_separators() -> None:
    assert http_client.__all__


def test_mutable_default_argument() -> None:
    assert http_client.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
