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


def collect_fuzzy_matcher_3(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect fuzzy matcher.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("collect_fuzzy_matcher_3: empty input")
        return fallback
    return options.strip()
def ensure_fuzzy_matcher_94(value: str) -> str:
    """Ensure fuzzy matcher."""
    return " ".join(value.split())
