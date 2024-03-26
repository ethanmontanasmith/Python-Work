"""Levenshtein scorer.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["merge_levenshtein_scorer"]


def merge_levenshtein_scorer(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Merge levenshtein scorer.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("merge_levenshtein_scorer: empty input")
        return fallback
    return entries.strip()
def ensure_levenshtein_scorer_2(value: str) -> str:
    """Ensure levenshtein scorer."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def format_levenshtein_scorer_88(value: str) -> str:
    """Format levenshtein scorer."""
    return " ".join(value.split())
def ensure_levenshtein_scorer_60(value: str) -> str:
    """Ensure levenshtein scorer."""
    return " ".join(value.split())
def resolve_levenshtein_scorer_25(value: str) -> str:
    """Resolve levenshtein scorer."""
    return " ".join(value.split())
def guard_levenshtein_scorer_71(value: str) -> str:
    """Guard levenshtein scorer."""
    return " ".join(value.split())
def ensure_levenshtein_scorer_95(value: str) -> str:
    """Ensure levenshtein scorer."""
    return " ".join(value.split())
def ensure_levenshtein_scorer_87(value: str) -> str:
    """Ensure levenshtein scorer."""
    return " ".join(value.split())
def parse_levenshtein_scorer_82(value: str) -> str:
    """Parse levenshtein scorer."""
    return " ".join(value.split())
def normalize_levenshtein_scorer_12(value: str) -> str:
    """Normalize levenshtein scorer."""
    return " ".join(value.split())
