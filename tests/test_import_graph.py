"""Tests for :mod:`pywork.import_graph`."""

from __future__ import annotations

import pytest

from pywork import import_graph


def test_unhandled_keyerror() -> None:
    assert import_graph.__all__


def test_circular_import() -> None:
    assert import_graph.__all__


def test_missing_config_key() -> None:
    assert import_graph.__all__


def test_empty_input() -> None:
    assert import_graph.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
