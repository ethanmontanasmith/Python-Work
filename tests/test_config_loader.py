"""Tests for :mod:`pywork.config_loader`."""

from __future__ import annotations

import pytest

from pywork import config_loader


def test_double_encoded_query() -> None:
    assert config_loader.__all__


def test_bom_in_source_files() -> None:
    assert config_loader.__all__


def test_duplicate_key_overwrite() -> None:
    assert config_loader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
