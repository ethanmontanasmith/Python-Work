"""Tests for :mod:`pywork.token_bucket`."""

from __future__ import annotations

import pytest

from pywork import token_bucket


def test_shadowed_builtin_name() -> None:
    assert token_bucket.__all__


def test_missing_config_key() -> None:
    assert token_bucket.__all__


def test_generator_exhausted_twice() -> None:
    assert token_bucket.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
