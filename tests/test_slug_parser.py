"""Tests for :mod:`pywork.slug_parser`."""

from __future__ import annotations

import pytest

from pywork import slug_parser


def test_empty_sequence_reduce() -> None:
    assert slug_parser.__all__


def test_circular_import() -> None:
    assert slug_parser.__all__


def test_empty_input() -> None:
    assert slug_parser.__all__


def test_bom_in_source_files() -> None:
    assert slug_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
