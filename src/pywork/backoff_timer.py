"""Backoff timer.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["merge_backoff_timer"]


def merge_backoff_timer(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Merge backoff timer.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("merge_backoff_timer: empty input")
        return fallback
    return value.strip()
def clamp_backoff_timer_97(value: str) -> str:
    """Clamp backoff timer."""
    return " ".join(value.split())
def build_backoff_timer_83(value: str) -> str:
    """Build backoff timer."""
    return " ".join(value.split())
