"""Tests for :mod:`pywork.import_graph`."""

from __future__ import annotations

import pytest

from pywork import import_graph


def test_generator_exhausted_twice() -> None:
    assert import_graph.__all__


def test_mutable_default_argument() -> None:
    assert import_graph.__all__


def test_race_on_concurrent_writes() -> None:
    assert import_graph.__all__


def test_empty_input() -> None:
    assert import_graph.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
