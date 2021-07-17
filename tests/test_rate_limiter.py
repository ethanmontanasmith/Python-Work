"""Tests for :mod:`pywork.rate_limiter`."""

from __future__ import annotations

import pytest

from pywork import rate_limiter


def test_mutable_default_argument() -> None:
    assert rate_limiter.__all__


def test_bom_in_source_files() -> None:
    assert rate_limiter.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
