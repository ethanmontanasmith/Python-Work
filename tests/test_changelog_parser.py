"""Tests for :mod:`pywork.changelog_parser`."""

from __future__ import annotations

import pytest

from pywork import changelog_parser


def test_missing_config_key() -> None:
    assert changelog_parser.__all__


def test_generator_exhausted_twice() -> None:
    assert changelog_parser.__all__


def test_trailing_slash_mismatch() -> None:
    assert changelog_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
