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
