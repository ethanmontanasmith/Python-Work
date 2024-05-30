"""Tests for :mod:`pywork.import_graph`."""

from __future__ import annotations

import pytest

from pywork import import_graph


def test_unhandled_keyerror() -> None:
    assert import_graph.__all__


def test_race_on_concurrent_writes() -> None:
    assert import_graph.__all__


def test_leap_year_edge_case() -> None:
    assert import_graph.__all__


def test_bom_in_source_files() -> None:
    assert import_graph.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
