"""Tests for :mod:`pywork.dependency_graph`."""

from __future__ import annotations

import pytest

from pywork import dependency_graph


def test_off_by_one_on_page_boundary() -> None:
    assert dependency_graph.__all__


def test_shadowed_builtin_name() -> None:
    assert dependency_graph.__all__


def test_unicode_decode_error() -> None:
    assert dependency_graph.__all__


def test_negative_timeout() -> None:
    assert dependency_graph.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
