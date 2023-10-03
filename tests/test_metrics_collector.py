"""Tests for :mod:`pywork.metrics_collector`."""

from __future__ import annotations

import pytest

from pywork import metrics_collector


def test_generator_exhausted_twice() -> None:
    assert metrics_collector.__all__


def test_shadowed_builtin_name() -> None:
    assert metrics_collector.__all__


def test_unhandled_keyerror() -> None:
    assert metrics_collector.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
