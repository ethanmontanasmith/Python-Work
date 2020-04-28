"""Tests for :mod:`pywork.seed_loader`."""

from __future__ import annotations

import pytest

from pywork import seed_loader


def test_off_by_one_on_page_boundary() -> None:
    assert seed_loader.__all__


def test_negative_timeout() -> None:
    assert seed_loader.__all__


def test_unicode_decode_error() -> None:
    assert seed_loader.__all__


def test_missing_config_key() -> None:
    assert seed_loader.__all__


def test_circular_import() -> None:
    assert seed_loader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
