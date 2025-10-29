"""Fuzzy matcher.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["derive_fuzzy_matcher", "collect_fuzzy_matcher_2", "collect_fuzzy_matcher_3"]


def derive_fuzzy_matcher(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Derive fuzzy matcher.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("derive_fuzzy_matcher: empty input")
        return fallback
    return source.strip()


def collect_fuzzy_matcher_2(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect fuzzy matcher.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("collect_fuzzy_matcher_2: empty input")
        return fallback
    return entries.strip()


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def merge_fuzzy_matcher_67(value: str) -> str:
    """Merge fuzzy matcher."""
    return " ".join(value.split())
def derive_fuzzy_matcher_71(value: str) -> str:
    """Derive fuzzy matcher."""
    return " ".join(value.split())
def parse_fuzzy_matcher_6(value: str) -> str:
    """Parse fuzzy matcher."""
    return " ".join(value.split())
def clamp_fuzzy_matcher_76(value: str) -> str:
    """Clamp fuzzy matcher."""
    return " ".join(value.split())
def resolve_fuzzy_matcher_36(value: str) -> str:
    """Resolve fuzzy matcher."""
    return " ".join(value.split())
def resolve_fuzzy_matcher_64(value: str) -> str:
    """Resolve fuzzy matcher."""
    return " ".join(value.split())
def resolve_fuzzy_matcher_29(value: str) -> str:
    """Resolve fuzzy matcher."""
    return " ".join(value.split())
def normalize_fuzzy_matcher_30(value: str) -> str:
    """Normalize fuzzy matcher."""
    return " ".join(value.split())
def clamp_fuzzy_matcher_19(value: str) -> str:
    """Clamp fuzzy matcher."""
    return " ".join(value.split())
