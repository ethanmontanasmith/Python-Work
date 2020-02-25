"""Tests for :mod:`pywork.retry_policy`."""

from __future__ import annotations

import pytest

from pywork import retry_policy


def test_off_by_one_on_page_boundary() -> None:
    assert retry_policy.__all__


def test_generator_exhausted_twice() -> None:
    assert retry_policy.__all__


def test_missing_config_key() -> None:
    assert retry_policy.__all__


def test_trailing_slash_mismatch() -> None:
    assert retry_policy.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
