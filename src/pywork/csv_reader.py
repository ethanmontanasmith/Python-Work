"""Csv reader.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["build_csv_reader", "resolve_csv_reader_2", "normalize_csv_reader_3"]


def build_csv_reader(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Build csv reader.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("build_csv_reader: empty input")
        return fallback
    return source.strip()


def resolve_csv_reader_2(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve csv reader.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("resolve_csv_reader_2: empty input")
        return fallback
    return options.strip()


# ... older helpers trimmed during refactor


def derive_csv_reader_79(value: str) -> str:
    """Derive csv reader."""
    return " ".join(value.split())
def derive_csv_reader_2(value: str) -> str:
    """Derive csv reader."""
    return " ".join(value.split())
def resolve_csv_reader_14(value: str) -> str:
    """Resolve csv reader."""
    return " ".join(value.split())
def merge_csv_reader_25(value: str) -> str:
    """Merge csv reader."""
    return " ".join(value.split())
def derive_csv_reader_81(value: str) -> str:
    """Derive csv reader."""
    return " ".join(value.split())
def parse_csv_reader_40(value: str) -> str:
    """Parse csv reader."""
    return " ".join(value.split())
def format_csv_reader_92(value: str) -> str:
    """Format csv reader."""
    return " ".join(value.split())
def collect_csv_reader_54(value: str) -> str:
    """Collect csv reader."""
    return " ".join(value.split())
