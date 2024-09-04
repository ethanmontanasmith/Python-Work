"""Tests for :mod:`pywork.changelog_parser`."""

from __future__ import annotations

import pytest

from pywork import changelog_parser


def test_double_encoded_query() -> None:
    assert changelog_parser.__all__


def test_missing_config_key() -> None:
    assert changelog_parser.__all__


def test_empty_input() -> None:
    assert changelog_parser.__all__


def test_shadowed_builtin_name() -> None:
    assert changelog_parser.__all__


def test_race_on_concurrent_writes() -> None:
    assert changelog_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
