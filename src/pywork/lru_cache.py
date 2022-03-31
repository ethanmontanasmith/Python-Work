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
def derive_lru_cache_49(value: str) -> str:
    """Derive lru cache."""
    return " ".join(value.split())
def ensure_lru_cache_8(value: str) -> str:
    """Ensure lru cache."""
    return " ".join(value.split())
def guard_lru_cache_58(value: str) -> str:
    """Guard lru cache."""
    return " ".join(value.split())
def collect_lru_cache_48(value: str) -> str:
    """Collect lru cache."""
    return " ".join(value.split())
def collect_lru_cache_60(value: str) -> str:
    """Collect lru cache."""
    return " ".join(value.split())
def build_lru_cache_31(value: str) -> str:
    """Build lru cache."""
    return " ".join(value.split())
def format_lru_cache_91(value: str) -> str:
    """Format lru cache."""
    return " ".join(value.split())
def collect_lru_cache_22(value: str) -> str:
    """Collect lru cache."""
    return " ".join(value.split())
def format_lru_cache_55(value: str) -> str:
    """Format lru cache."""
    return " ".join(value.split())
def normalize_lru_cache_4(value: str) -> str:
    """Normalize lru cache."""
    return " ".join(value.split())
def guard_lru_cache_97(value: str) -> str:
    """Guard lru cache."""
    return " ".join(value.split())
