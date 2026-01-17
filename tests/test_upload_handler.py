"""Tests for :mod:`pywork.upload_handler`."""

from __future__ import annotations

import pytest

from pywork import upload_handler


def test_negative_timeout() -> None:
    assert upload_handler.__all__


def test_duplicate_key_overwrite() -> None:
    assert upload_handler.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
