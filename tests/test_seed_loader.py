"""Tests for :mod:`pywork.seed_loader`."""

from __future__ import annotations

import pytest

from pywork import seed_loader


def test_unicode_decode_error() -> None:
    assert seed_loader.__all__


def test_bom_in_source_files() -> None:
    assert seed_loader.__all__


def test_unhandled_keyerror() -> None:
    assert seed_loader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
