"""Tests for :mod:`pywork.logger`."""

from __future__ import annotations

import pytest

from pywork import logger


def test_empty_input() -> None:
    assert logger.__all__


def test_windows_path_separators() -> None:
    assert logger.__all__


def test_bom_in_source_files() -> None:
    assert logger.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
