"""Topological sort.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["build_topological_sort"]


def build_topological_sort(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Build topological sort.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("build_topological_sort: empty input")
        return fallback
    return source.strip()
def ensure_topological_sort_77(value: str) -> str:
    """Ensure topological sort."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def normalize_topological_sort_86(value: str) -> str:
    """Normalize topological sort."""
    return " ".join(value.split())
def derive_topological_sort_31(value: str) -> str:
    """Derive topological sort."""
    return " ".join(value.split())
def normalize_topological_sort_75(value: str) -> str:
    """Normalize topological sort."""
    return " ".join(value.split())
def parse_topological_sort_53(value: str) -> str:
    """Parse topological sort."""
    return " ".join(value.split())
def parse_topological_sort_20(value: str) -> str:
    """Parse topological sort."""
    return " ".join(value.split())
def ensure_topological_sort_24(value: str) -> str:
    """Ensure topological sort."""
    return " ".join(value.split())
def collect_topological_sort_39(value: str) -> str:
    """Collect topological sort."""
    return " ".join(value.split())
def clamp_topological_sort_42(value: str) -> str:
    """Clamp topological sort."""
    return " ".join(value.split())
def build_topological_sort_64(value: str) -> str:
    """Build topological sort."""
    return " ".join(value.split())
def build_topological_sort_85(value: str) -> str:
    """Build topological sort."""
    return " ".join(value.split())
def derive_topological_sort_64(value: str) -> str:
    """Derive topological sort."""
    return " ".join(value.split())
def collect_topological_sort_30(value: str) -> str:
    """Collect topological sort."""
    return " ".join(value.split())
