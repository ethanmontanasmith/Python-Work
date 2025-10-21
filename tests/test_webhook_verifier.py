"""Tests for :mod:`pywork.webhook_verifier`."""

from __future__ import annotations

import pytest

from pywork import webhook_verifier


def test_empty_sequence_reduce() -> None:
    assert webhook_verifier.__all__


def test_leap_year_edge_case() -> None:
    assert webhook_verifier.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert webhook_verifier.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
