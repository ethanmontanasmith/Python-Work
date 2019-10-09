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
