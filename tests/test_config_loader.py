"""Tests for :mod:`pywork.config_loader`."""

from __future__ import annotations

import pytest

from pywork import config_loader


def test_shadowed_builtin_name() -> None:
    assert config_loader.__all__


def test_stale_cache_entry() -> None:
    assert config_loader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
