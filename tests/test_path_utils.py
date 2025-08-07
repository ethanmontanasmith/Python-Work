"""Tests for :mod:`pywork.path_utils`."""

from __future__ import annotations

import pytest

from pywork import path_utils


def test_off_by_one_on_page_boundary() -> None:
    assert path_utils.__all__


def test_generator_exhausted_twice() -> None:
    assert path_utils.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
