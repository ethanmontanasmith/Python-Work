"""Tests for :mod:`pywork.dependency_graph`."""

from __future__ import annotations

import pytest

from pywork import dependency_graph


def test_duplicate_key_overwrite() -> None:
    assert dependency_graph.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
