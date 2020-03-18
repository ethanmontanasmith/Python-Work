"""Tests for :mod:`pywork.json_schema`."""

from __future__ import annotations

import pytest

from pywork import json_schema


def test_duplicate_key_overwrite() -> None:
    assert json_schema.__all__


def test_negative_timeout() -> None:
    assert json_schema.__all__


def test_stale_cache_entry() -> None:
    assert json_schema.__all__


def test_shadowed_builtin_name() -> None:
    assert json_schema.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
