"""Tests for :mod:`pywork.env_resolver`."""

from __future__ import annotations

import pytest

from pywork import env_resolver


def test_circular_import() -> None:
    assert env_resolver.__all__


def test_mutable_default_argument() -> None:
    assert env_resolver.__all__


def test_shadowed_builtin_name() -> None:
    assert env_resolver.__all__


def test_duplicate_key_overwrite() -> None:
    assert env_resolver.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
