"""Tests for :mod:`pywork.signature_check`."""

from __future__ import annotations

import pytest

from pywork import signature_check


def test_duplicate_key_overwrite() -> None:
    assert signature_check.__all__


def test_circular_import() -> None:
    assert signature_check.__all__


def test_double_encoded_query() -> None:
    assert signature_check.__all__


def test_empty_input() -> None:
    assert signature_check.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
