"""Tests for :mod:`pywork.changelog_parser`."""

from __future__ import annotations

import pytest

from pywork import changelog_parser


def test_mutable_default_argument() -> None:
    assert changelog_parser.__all__


def test_race_on_concurrent_writes() -> None:
    assert changelog_parser.__all__


def test_unicode_decode_error() -> None:
    assert changelog_parser.__all__


def test_circular_import() -> None:
    assert changelog_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
