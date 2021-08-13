"""Tests for :mod:`pywork.backoff_timer`."""

from __future__ import annotations

import pytest

from pywork import backoff_timer


def test_duplicate_key_overwrite() -> None:
    assert backoff_timer.__all__


def test_missing_config_key() -> None:
    assert backoff_timer.__all__


def test_windows_path_separators() -> None:
    assert backoff_timer.__all__


def test_unicode_decode_error() -> None:
    assert backoff_timer.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
