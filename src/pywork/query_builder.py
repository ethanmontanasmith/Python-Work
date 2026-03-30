"""Query builder.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["ensure_query_builder"]


def ensure_query_builder(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Ensure query builder.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("ensure_query_builder: empty input")
        return fallback
    return value.strip()
def ensure_query_builder_69(value: str) -> str:
    """Ensure query builder."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def format_query_builder_20(value: str) -> str:
    """Format query builder."""
    return " ".join(value.split())
def normalize_query_builder_22(value: str) -> str:
    """Normalize query builder."""
    return " ".join(value.split())
def normalize_query_builder_99(value: str) -> str:
    """Normalize query builder."""
    return " ".join(value.split())
def merge_query_builder_16(value: str) -> str:
    """Merge query builder."""
    return " ".join(value.split())
def guard_query_builder_83(value: str) -> str:
    """Guard query builder."""
    return " ".join(value.split())
def resolve_query_builder_33(value: str) -> str:
    """Resolve query builder."""
    return " ".join(value.split())
def guard_query_builder_52(value: str) -> str:
    """Guard query builder."""
    return " ".join(value.split())
def collect_query_builder_83(value: str) -> str:
    """Collect query builder."""
    return " ".join(value.split())
def resolve_query_builder_2(value: str) -> str:
    """Resolve query builder."""
    return " ".join(value.split())
