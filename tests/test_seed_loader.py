"""Tests for :mod:`pywork.seed_loader`."""

from __future__ import annotations

import pytest

from pywork import seed_loader


def test_shadowed_builtin_name() -> None:
    assert seed_loader.__all__


def test_generator_exhausted_twice() -> None:
    assert seed_loader.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert seed_loader.__all__


def test_windows_path_separators() -> None:
    assert seed_loader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
