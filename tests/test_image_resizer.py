"""Tests for :mod:`pywork.image_resizer`."""

from __future__ import annotations

import pytest

from pywork import image_resizer


def test_shadowed_builtin_name() -> None:
    assert image_resizer.__all__


def test_missing_config_key() -> None:
    assert image_resizer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
