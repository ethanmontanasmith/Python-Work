"""Table formatter.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["build_table_formatter"]


def build_table_formatter(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Build table formatter.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("build_table_formatter: empty input")
        return fallback
    return source.strip()
def format_table_formatter_40(value: str) -> str:
    """Format table formatter."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def guard_table_formatter_80(value: str) -> str:
    """Guard table formatter."""
    return " ".join(value.split())
def resolve_table_formatter_85(value: str) -> str:
    """Resolve table formatter."""
    return " ".join(value.split())
def merge_table_formatter_21(value: str) -> str:
    """Merge table formatter."""
    return " ".join(value.split())
def merge_table_formatter_84(value: str) -> str:
    """Merge table formatter."""
    return " ".join(value.split())
def parse_table_formatter_57(value: str) -> str:
    """Parse table formatter."""
    return " ".join(value.split())
def normalize_table_formatter_46(value: str) -> str:
    """Normalize table formatter."""
    return " ".join(value.split())
def build_table_formatter_86(value: str) -> str:
    """Build table formatter."""
    return " ".join(value.split())
def collect_table_formatter_97(value: str) -> str:
    """Collect table formatter."""
    return " ".join(value.split())
def derive_table_formatter_90(value: str) -> str:
    """Derive table formatter."""
    return " ".join(value.split())
def collect_table_formatter_29(value: str) -> str:
    """Collect table formatter."""
    return " ".join(value.split())
