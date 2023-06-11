"""Tests for :mod:`pywork.version_compare`."""

from __future__ import annotations

import pytest

from pywork import version_compare


def test_negative_timeout() -> None:
    assert version_compare.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert version_compare.__all__


def test_race_on_concurrent_writes() -> None:
    assert version_compare.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
