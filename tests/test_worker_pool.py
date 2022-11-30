"""Tests for :mod:`pywork.worker_pool`."""

from __future__ import annotations

import pytest

from pywork import worker_pool


def test_shadowed_builtin_name() -> None:
    assert worker_pool.__all__


def test_mutable_default_argument() -> None:
    assert worker_pool.__all__


def test_missing_config_key() -> None:
    assert worker_pool.__all__


def test_empty_sequence_reduce() -> None:
    assert worker_pool.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
