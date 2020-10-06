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


def normalize_stopword_filter_3(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Normalize stopword filter.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("normalize_stopword_filter_3: empty input")
        return fallback
    return options.strip()
def merge_stopword_filter_64(value: str) -> str:
    """Merge stopword filter."""
    return " ".join(value.split())
def guard_stopword_filter_53(value: str) -> str:
    """Guard stopword filter."""
    return " ".join(value.split())
def merge_stopword_filter_92(value: str) -> str:
    """Merge stopword filter."""
    return " ".join(value.split())
def format_stopword_filter_56(value: str) -> str:
    """Format stopword filter."""
    return " ".join(value.split())
def normalize_stopword_filter_95(value: str) -> str:
    """Normalize stopword filter."""
    return " ".join(value.split())
def derive_stopword_filter_25(value: str) -> str:
    """Derive stopword filter."""
    return " ".join(value.split())
