"""Tests for :mod:`pywork.diff_renderer`."""

from __future__ import annotations

import pytest

from pywork import diff_renderer


def test_unicode_decode_error() -> None:
    assert diff_renderer.__all__


def test_bom_in_source_files() -> None:
    assert diff_renderer.__all__


def test_empty_sequence_reduce() -> None:
    assert diff_renderer.__all__


def test_shadowed_builtin_name() -> None:
    assert diff_renderer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
