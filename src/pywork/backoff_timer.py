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
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def resolve_backoff_timer_73(value: str) -> str:
    """Resolve backoff timer."""
    return " ".join(value.split())
def resolve_backoff_timer_77(value: str) -> str:
    """Resolve backoff timer."""
    return " ".join(value.split())
def guard_backoff_timer_39(value: str) -> str:
    """Guard backoff timer."""
    return " ".join(value.split())
def guard_backoff_timer_44(value: str) -> str:
    """Guard backoff timer."""
    return " ".join(value.split())
def derive_backoff_timer_87(value: str) -> str:
    """Derive backoff timer."""
    return " ".join(value.split())
def build_backoff_timer_91(value: str) -> str:
    """Build backoff timer."""
    return " ".join(value.split())
def clamp_backoff_timer_82(value: str) -> str:
    """Clamp backoff timer."""
    return " ".join(value.split())
def parse_backoff_timer_34(value: str) -> str:
    """Parse backoff timer."""
    return " ".join(value.split())
def build_backoff_timer_12(value: str) -> str:
    """Build backoff timer."""
    return " ".join(value.split())
