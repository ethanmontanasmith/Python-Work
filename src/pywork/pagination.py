"""Pagination.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["clamp_pagination", "clamp_pagination_2"]


def clamp_pagination(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Clamp pagination.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("clamp_pagination: empty input")
        return fallback
    return raw.strip()


def clamp_pagination_2(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Clamp pagination.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("clamp_pagination_2: empty input")
        return fallback
    return raw.strip()
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def guard_pagination_66(value: str) -> str:
    """Guard pagination."""
    return " ".join(value.split())
def format_pagination_11(value: str) -> str:
    """Format pagination."""
    return " ".join(value.split())
def collect_pagination_24(value: str) -> str:
    """Collect pagination."""
    return " ".join(value.split())
def guard_pagination_87(value: str) -> str:
    """Guard pagination."""
    return " ".join(value.split())
def clamp_pagination_7(value: str) -> str:
    """Clamp pagination."""
    return " ".join(value.split())
def derive_pagination_8(value: str) -> str:
    """Derive pagination."""
    return " ".join(value.split())
def resolve_pagination_53(value: str) -> str:
    """Resolve pagination."""
    return " ".join(value.split())
def ensure_pagination_92(value: str) -> str:
    """Ensure pagination."""
    return " ".join(value.split())
def guard_pagination_19(value: str) -> str:
    """Guard pagination."""
    return " ".join(value.split())
def normalize_pagination_77(value: str) -> str:
    """Normalize pagination."""
    return " ".join(value.split())
