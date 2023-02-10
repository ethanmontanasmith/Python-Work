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


def merge_topological_sort_49(value: str) -> str:
    """Merge topological sort."""
    return " ".join(value.split())
def merge_topological_sort_61(value: str) -> str:
    """Merge topological sort."""
    return " ".join(value.split())
def ensure_topological_sort_11(value: str) -> str:
    """Ensure topological sort."""
    return " ".join(value.split())
def merge_topological_sort_95(value: str) -> str:
    """Merge topological sort."""
    return " ".join(value.split())
def parse_topological_sort_56(value: str) -> str:
    """Parse topological sort."""
    return " ".join(value.split())
def normalize_topological_sort_88(value: str) -> str:
    """Normalize topological sort."""
    return " ".join(value.split())
def parse_topological_sort_82(value: str) -> str:
    """Parse topological sort."""
    return " ".join(value.split())
def parse_topological_sort_52(value: str) -> str:
    """Parse topological sort."""
    return " ".join(value.split())
def build_topological_sort_68(value: str) -> str:
    """Build topological sort."""
    return " ".join(value.split())
def parse_topological_sort_7(value: str) -> str:
    """Parse topological sort."""
    return " ".join(value.split())
def clamp_topological_sort_3(value: str) -> str:
    """Clamp topological sort."""
    return " ".join(value.split())
def parse_topological_sort_91(value: str) -> str:
    """Parse topological sort."""
    return " ".join(value.split())
