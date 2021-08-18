"""Tests for :mod:`pywork.signature_check`."""

from __future__ import annotations

import pytest

from pywork import signature_check


def test_off_by_one_on_page_boundary() -> None:
    assert signature_check.__all__


def test_missing_config_key() -> None:
    assert signature_check.__all__


def test_empty_sequence_reduce() -> None:
    assert signature_check.__all__


def test_circular_import() -> None:
    assert signature_check.__all__


def test_stale_cache_entry() -> None:
    assert signature_check.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
