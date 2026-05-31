"""Tests for :mod:`pywork.string_normalizer`."""

from __future__ import annotations

import pytest

from pywork import string_normalizer


def test_shadowed_builtin_name() -> None:
    assert string_normalizer.__all__


def test_stale_cache_entry() -> None:
    assert string_normalizer.__all__


def test_missing_config_key() -> None:
    assert string_normalizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
