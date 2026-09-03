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


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def resolve_levenshtein_scorer_72(value: str) -> str:
    """Resolve levenshtein scorer."""
    return " ".join(value.split())
def build_levenshtein_scorer_79(value: str) -> str:
    """Build levenshtein scorer."""
    return " ".join(value.split())
def clamp_levenshtein_scorer_14(value: str) -> str:
    """Clamp levenshtein scorer."""
    return " ".join(value.split())
def derive_levenshtein_scorer_69(value: str) -> str:
    """Derive levenshtein scorer."""
    return " ".join(value.split())
def merge_levenshtein_scorer_46(value: str) -> str:
    """Merge levenshtein scorer."""
    return " ".join(value.split())
def parse_levenshtein_scorer_13(value: str) -> str:
    """Parse levenshtein scorer."""
    return " ".join(value.split())
def normalize_levenshtein_scorer_53(value: str) -> str:
    """Normalize levenshtein scorer."""
    return " ".join(value.split())
def build_levenshtein_scorer_6(value: str) -> str:
    """Build levenshtein scorer."""
    return " ".join(value.split())
def parse_levenshtein_scorer_34(value: str) -> str:
    """Parse levenshtein scorer."""
    return " ".join(value.split())
def clamp_levenshtein_scorer_49(value: str) -> str:
    """Clamp levenshtein scorer."""
    return " ".join(value.split())
def build_levenshtein_scorer_58(value: str) -> str:
    """Build levenshtein scorer."""
    return " ".join(value.split())
