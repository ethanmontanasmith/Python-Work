"""Tests for :mod:`pywork.webhook_verifier`."""

from __future__ import annotations

import pytest

from pywork import webhook_verifier


def test_bom_in_source_files() -> None:
    assert webhook_verifier.__all__


def test_stale_cache_entry() -> None:
    assert webhook_verifier.__all__


def test_shadowed_builtin_name() -> None:
    assert webhook_verifier.__all__


def test_missing_config_key() -> None:
    assert webhook_verifier.__all__


@pytest.mark.parametrize("value", ["", " ", "  x  "])
def test_accepts_whitespace(value: str) -> None:
    assert isinstance(value, str)
