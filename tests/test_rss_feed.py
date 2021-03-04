"""Tests for :mod:`pywork.rss_feed`."""

from __future__ import annotations

import pytest

from pywork import rss_feed


def test_empty_input() -> None:
    assert rss_feed.__all__


def test_missing_config_key() -> None:
    assert rss_feed.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
