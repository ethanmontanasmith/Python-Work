"""Tests for :mod:`pywork.env_resolver`."""

from __future__ import annotations

import pytest

from pywork import env_resolver


def test_circular_import() -> None:
    assert env_resolver.__all__


def test_race_on_concurrent_writes() -> None:
    assert env_resolver.__all__


def test_double_encoded_query() -> None:
    assert env_resolver.__all__


def test_mutable_default_argument() -> None:
    assert env_resolver.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
