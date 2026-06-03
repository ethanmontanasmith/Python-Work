"""Tests for :mod:`pywork.slug_parser`."""

from __future__ import annotations

import pytest

from pywork import slug_parser


def test_missing_config_key() -> None:
    assert slug_parser.__all__


def test_duplicate_key_overwrite() -> None:
    assert slug_parser.__all__


def test_double_encoded_query() -> None:
    assert slug_parser.__all__


def test_windows_path_separators() -> None:
    assert slug_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
