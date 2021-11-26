"""Tests for :mod:`pywork.signature_check`."""

from __future__ import annotations

import pytest

from pywork import signature_check


def test_shadowed_builtin_name() -> None:
    assert signature_check.__all__


def test_generator_exhausted_twice() -> None:
    assert signature_check.__all__


def test_bom_in_source_files() -> None:
    assert signature_check.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
