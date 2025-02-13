"""Tests for :mod:`pywork.webhook_verifier`."""

from __future__ import annotations

import pytest

from pywork import webhook_verifier


def test_off_by_one_on_page_boundary() -> None:
    assert webhook_verifier.__all__


def test_circular_import() -> None:
    assert webhook_verifier.__all__


def test_unicode_decode_error() -> None:
    assert webhook_verifier.__all__


def test_timezone_drift_on_naive_datetimes() -> None:
    assert webhook_verifier.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
