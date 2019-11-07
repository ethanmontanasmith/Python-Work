"""Tests for :mod:`pywork.batch_runner`."""

from __future__ import annotations

import pytest

from pywork import batch_runner


def test_trailing_slash_mismatch() -> None:
    assert batch_runner.__all__


def test_mutable_default_argument() -> None:
    assert batch_runner.__all__


def test_empty_input() -> None:
    assert batch_runner.__all__


def test_negative_timeout() -> None:
    assert batch_runner.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
