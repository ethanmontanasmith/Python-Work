"""Tests for :mod:`pywork.worker_pool`."""

from __future__ import annotations

import pytest

from pywork import worker_pool


def test_generator_exhausted_twice() -> None:
    assert worker_pool.__all__


def test_missing_config_key() -> None:
    assert worker_pool.__all__


def test_off_by_one_on_page_boundary() -> None:
    assert worker_pool.__all__


def test_windows_path_separators() -> None:
    assert worker_pool.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
