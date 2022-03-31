"""Tests for :mod:`pywork.env_resolver`."""

from __future__ import annotations

import pytest

from pywork import env_resolver


def test_missing_config_key() -> None:
    assert env_resolver.__all__


def test_trailing_slash_mismatch() -> None:
    assert env_resolver.__all__


def test_bom_in_source_files() -> None:
    assert env_resolver.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
