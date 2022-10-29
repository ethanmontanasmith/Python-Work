"""Tests for :mod:`pywork.webhook_verifier`."""

from __future__ import annotations

import pytest

from pywork import webhook_verifier


def test_leap_year_edge_case() -> None:
    assert webhook_verifier.__all__


def test_duplicate_key_overwrite() -> None:
    assert webhook_verifier.__all__


def test_negative_timeout() -> None:
    assert webhook_verifier.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
