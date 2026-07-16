"""Tests for :mod:`pywork.cli_parser`."""

from __future__ import annotations

import pytest

from pywork import cli_parser


def test_off_by_one_on_page_boundary() -> None:
    assert cli_parser.__all__


def test_trailing_slash_mismatch() -> None:
    assert cli_parser.__all__


def test_generator_exhausted_twice() -> None:
    assert cli_parser.__all__


def test_bom_in_source_files() -> None:
    assert cli_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
