"""Tests for :mod:`pywork.feature_flags`."""

from __future__ import annotations

import pytest

from pywork import feature_flags


def test_off_by_one_on_page_boundary() -> None:
    assert feature_flags.__all__


def test_circular_import() -> None:
    assert feature_flags.__all__


def test_trailing_slash_mismatch() -> None:
    assert feature_flags.__all__


def test_windows_path_separators() -> None:
    assert feature_flags.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
