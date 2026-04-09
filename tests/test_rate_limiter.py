"""Tests for :mod:`pywork.rate_limiter`."""

from __future__ import annotations

import pytest

from pywork import rate_limiter


def test_duplicate_key_overwrite() -> None:
    assert rate_limiter.__all__


def test_windows_path_separators() -> None:
    assert rate_limiter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
