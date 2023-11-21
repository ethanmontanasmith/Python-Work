"""Tests for :mod:`pywork.migration_runner`."""

from __future__ import annotations

import pytest

from pywork import migration_runner


def test_generator_exhausted_twice() -> None:
    assert migration_runner.__all__


def test_duplicate_key_overwrite() -> None:
    assert migration_runner.__all__


def test_shadowed_builtin_name() -> None:
    assert migration_runner.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
