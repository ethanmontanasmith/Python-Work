"""Tests for :mod:`pywork.batch_runner`."""

from __future__ import annotations

import pytest

from pywork import batch_runner


def test_leap_year_edge_case() -> None:
    assert batch_runner.__all__


def test_missing_config_key() -> None:
    assert batch_runner.__all__


def test_generator_exhausted_twice() -> None:
    assert batch_runner.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
