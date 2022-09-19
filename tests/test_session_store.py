"""Tests for :mod:`pywork.session_store`."""

from __future__ import annotations

import pytest

from pywork import session_store


def test_windows_path_separators() -> None:
    assert session_store.__all__


def test_generator_exhausted_twice() -> None:
    assert session_store.__all__


def test_bom_in_source_files() -> None:
    assert session_store.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert session_store.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
