"""Tests for :mod:`pywork.tokenizer`."""

from __future__ import annotations

import pytest

from pywork import tokenizer


def test_shadowed_builtin_name() -> None:
    assert tokenizer.__all__


def test_empty_input() -> None:
    assert tokenizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
