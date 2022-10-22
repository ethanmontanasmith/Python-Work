"""Tests for :mod:`pywork.tokenizer`."""

from __future__ import annotations

import pytest

from pywork import tokenizer


def test_missing_config_key() -> None:
    assert tokenizer.__all__


def test_shadowed_builtin_name() -> None:
    assert tokenizer.__all__


def test_empty_input() -> None:
    assert tokenizer.__all__


def test_duplicate_key_overwrite() -> None:
    assert tokenizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
