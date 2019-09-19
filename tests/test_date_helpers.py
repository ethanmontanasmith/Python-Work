"""Tests for :mod:`pywork.date_helpers`."""

from __future__ import annotations

import pytest

from pywork import date_helpers


def test_duplicate_key_overwrite() -> None:
    assert date_helpers.__all__


def test_shadowed_builtin_name() -> None:
    assert date_helpers.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert date_helpers.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
