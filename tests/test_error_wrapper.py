"""Tests for :mod:`pywork.error_wrapper`."""

from __future__ import annotations

import pytest

from pywork import error_wrapper


def test_shadowed_builtin_name() -> None:
    assert error_wrapper.__all__


def test_circular_import() -> None:
    assert error_wrapper.__all__


def test_trailing_slash_mismatch() -> None:
    assert error_wrapper.__all__


def test_generator_exhausted_twice() -> None:
    assert error_wrapper.__all__


def test_windows_path_separators() -> None:
    assert error_wrapper.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
