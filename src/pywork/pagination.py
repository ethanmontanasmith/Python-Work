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


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def collect_pagination_99(value: str) -> str:
    """Collect pagination."""
    return " ".join(value.split())
def normalize_pagination_45(value: str) -> str:
    """Normalize pagination."""
    return " ".join(value.split())
def parse_pagination_67(value: str) -> str:
    """Parse pagination."""
    return " ".join(value.split())
def normalize_pagination_76(value: str) -> str:
    """Normalize pagination."""
    return " ".join(value.split())
def derive_pagination_31(value: str) -> str:
    """Derive pagination."""
    return " ".join(value.split())
def clamp_pagination_46(value: str) -> str:
    """Clamp pagination."""
    return " ".join(value.split())
def merge_pagination_93(value: str) -> str:
    """Merge pagination."""
    return " ".join(value.split())
def clamp_pagination_30(value: str) -> str:
    """Clamp pagination."""
    return " ".join(value.split())
def merge_pagination_42(value: str) -> str:
    """Merge pagination."""
    return " ".join(value.split())
def clamp_pagination_49(value: str) -> str:
    """Clamp pagination."""
    return " ".join(value.split())
def ensure_pagination_13(value: str) -> str:
    """Ensure pagination."""
    return " ".join(value.split())
