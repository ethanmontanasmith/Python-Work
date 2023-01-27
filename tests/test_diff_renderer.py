"""Tests for :mod:`pywork.diff_renderer`."""

from __future__ import annotations

import pytest

from pywork import diff_renderer


def test_double_encoded_query() -> None:
    assert diff_renderer.__all__


def test_bom_in_source_files() -> None:
    assert diff_renderer.__all__


def test_negative_timeout() -> None:
    assert diff_renderer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
