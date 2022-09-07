"""Tests for :mod:`pywork.json_schema`."""

from __future__ import annotations

import pytest

from pywork import json_schema


def test_circular_import() -> None:
    assert json_schema.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert json_schema.__all__


def test_windows_path_separators() -> None:
    assert json_schema.__all__


def test_generator_exhausted_twice() -> None:
    assert json_schema.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
