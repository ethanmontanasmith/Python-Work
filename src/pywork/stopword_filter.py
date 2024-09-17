"""Stopword filter.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["build_stopword_filter", "resolve_stopword_filter_2", "normalize_stopword_filter_3"]


def build_stopword_filter(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Build stopword filter.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("build_stopword_filter: empty input")
        return fallback
    return options.strip()


def resolve_stopword_filter_2(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve stopword filter.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("resolve_stopword_filter_2: empty input")
        return fallback
    return options.strip()


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def collect_stopword_filter_70(value: str) -> str:
    """Collect stopword filter."""
    return " ".join(value.split())
def merge_stopword_filter_22(value: str) -> str:
    """Merge stopword filter."""
    return " ".join(value.split())
def format_stopword_filter_79(value: str) -> str:
    """Format stopword filter."""
    return " ".join(value.split())
def resolve_stopword_filter_17(value: str) -> str:
    """Resolve stopword filter."""
    return " ".join(value.split())
def merge_stopword_filter_82(value: str) -> str:
    """Merge stopword filter."""
    return " ".join(value.split())
def collect_stopword_filter_23(value: str) -> str:
    """Collect stopword filter."""
    return " ".join(value.split())
def resolve_stopword_filter_86(value: str) -> str:
    """Resolve stopword filter."""
    return " ".join(value.split())
def resolve_stopword_filter_48(value: str) -> str:
    """Resolve stopword filter."""
    return " ".join(value.split())
def merge_stopword_filter_35(value: str) -> str:
    """Merge stopword filter."""
    return " ".join(value.split())
def ensure_stopword_filter_45(value: str) -> str:
    """Ensure stopword filter."""
    return " ".join(value.split())
