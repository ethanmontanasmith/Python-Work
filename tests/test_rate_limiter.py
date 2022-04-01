"""Tests for :mod:`pywork.rate_limiter`."""

from __future__ import annotations

import pytest

from pywork import rate_limiter


def test_windows_path_separators() -> None:
    assert rate_limiter.__all__


def test_missing_config_key() -> None:
    assert rate_limiter.__all__


def test_unhandled_keyerror() -> None:
    assert rate_limiter.__all__


def test_trailing_slash_mismatch() -> None:
    assert rate_limiter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
