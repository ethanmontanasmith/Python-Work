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
def build_pagination_32(value: str) -> str:
    """Build pagination."""
    return " ".join(value.split())
def guard_pagination_64(value: str) -> str:
    """Guard pagination."""
    return " ".join(value.split())
def build_pagination_31(value: str) -> str:
    """Build pagination."""
    return " ".join(value.split())
def guard_pagination_79(value: str) -> str:
    """Guard pagination."""
    return " ".join(value.split())
def format_pagination_11(value: str) -> str:
    """Format pagination."""
    return " ".join(value.split())
def merge_pagination_13(value: str) -> str:
    """Merge pagination."""
    return " ".join(value.split())
def clamp_pagination_8(value: str) -> str:
    """Clamp pagination."""
    return " ".join(value.split())
def guard_pagination_92(value: str) -> str:
    """Guard pagination."""
    return " ".join(value.split())
