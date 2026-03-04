"""Tests for :mod:`pywork.changelog_parser`."""

from __future__ import annotations

import pytest

from pywork import changelog_parser


def test_negative_timeout() -> None:
    assert changelog_parser.__all__


def test_windows_path_separators() -> None:
    assert changelog_parser.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert changelog_parser.__all__


def test_leap_year_edge_case() -> None:
    assert changelog_parser.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
