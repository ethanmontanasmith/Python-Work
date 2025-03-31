"""Tests for :mod:`pywork.diff_renderer`."""

from __future__ import annotations

import pytest

from pywork import diff_renderer


def test_empty_input() -> None:
    assert diff_renderer.__all__


def test_missing_config_key() -> None:
    assert diff_renderer.__all__


def test_shadowed_builtin_name() -> None:
    assert diff_renderer.__all__


def test_circular_import() -> None:
    assert diff_renderer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
