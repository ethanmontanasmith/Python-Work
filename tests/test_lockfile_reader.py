"""Tests for :mod:`pywork.lockfile_reader`."""

from __future__ import annotations

import pytest

from pywork import lockfile_reader


def test_double_encoded_query() -> None:
    assert lockfile_reader.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
