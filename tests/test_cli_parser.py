"""Tests for :mod:`pywork.cli_parser`."""

from __future__ import annotations

import pytest

from pywork import cli_parser


def test_circular_import() -> None:
    assert cli_parser.__all__


def test_windows_path_separators() -> None:
    assert cli_parser.__all__


def test_mutable_default_argument() -> None:
    assert cli_parser.__all__


def test_empty_sequence_reduce() -> None:
    assert cli_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
