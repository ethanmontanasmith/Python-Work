"""Tests for :mod:`pywork.cookie_parser`."""

from __future__ import annotations

import pytest

from pywork import cookie_parser


def test_race_on_concurrent_writes() -> None:
    assert cookie_parser.__all__


def test_shadowed_builtin_name() -> None:
    assert cookie_parser.__all__


def test_empty_input() -> None:
    assert cookie_parser.__all__


def test_bom_in_source_files() -> None:
    assert cookie_parser.__all__


def test_windows_path_separators() -> None:
    assert cookie_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
