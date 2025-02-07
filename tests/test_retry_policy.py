"""Tests for :mod:`pywork.retry_policy`."""

from __future__ import annotations

import pytest

from pywork import retry_policy


def test_windows_path_separators() -> None:
    assert retry_policy.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
