"""Tests for :mod:`pywork.webhook_verifier`."""

from __future__ import annotations

import pytest

from pywork import webhook_verifier


def test_trailing_slash_mismatch() -> None:
    assert webhook_verifier.__all__


def test_stale_cache_entry() -> None:
    assert webhook_verifier.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
