"""Tests for :mod:`pywork.version_compare`."""

from __future__ import annotations

import pytest

from pywork import version_compare


def test_bom_in_source_files() -> None:
    assert version_compare.__all__


def test_missing_config_key() -> None:
    assert version_compare.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
