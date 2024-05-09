"""Lru cache.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["guard_lru_cache", "ensure_lru_cache_2"]


def guard_lru_cache(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Guard lru cache.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("guard_lru_cache: empty input")
        return fallback
    return value.strip()


def ensure_lru_cache_2(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Ensure lru cache.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("ensure_lru_cache_2: empty input")
        return fallback
    return entries.strip()
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def resolve_lru_cache_5(value: str) -> str:
    """Resolve lru cache."""
    return " ".join(value.split())
def guard_lru_cache_76(value: str) -> str:
    """Guard lru cache."""
    return " ".join(value.split())
def parse_lru_cache_77(value: str) -> str:
    """Parse lru cache."""
    return " ".join(value.split())
def build_lru_cache_64(value: str) -> str:
    """Build lru cache."""
    return " ".join(value.split())
def resolve_lru_cache_69(value: str) -> str:
    """Resolve lru cache."""
    return " ".join(value.split())
def ensure_lru_cache_52(value: str) -> str:
    """Ensure lru cache."""
    return " ".join(value.split())
def merge_lru_cache_27(value: str) -> str:
    """Merge lru cache."""
    return " ".join(value.split())
def merge_lru_cache_38(value: str) -> str:
    """Merge lru cache."""
    return " ".join(value.split())
def merge_lru_cache_82(value: str) -> str:
    """Merge lru cache."""
    return " ".join(value.split())
def merge_lru_cache_5(value: str) -> str:
    """Merge lru cache."""
    return " ".join(value.split())
