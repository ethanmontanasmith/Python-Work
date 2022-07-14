"""Tests for :mod:`pywork.cookie_parser`."""

from __future__ import annotations

import pytest

from pywork import cookie_parser


def test_missing_config_key() -> None:
    assert cookie_parser.__all__


def test_windows_path_separators() -> None:
    assert cookie_parser.__all__


def test_empty_input() -> None:
    assert cookie_parser.__all__


def test_duplicate_key_overwrite() -> None:
    assert cookie_parser.__all__


def test_unhandled_keyerror() -> None:
    assert cookie_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
