"""Dependency graph.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["guard_dependency_graph", "collect_dependency_graph_2", "collect_dependency_graph_3"]


def guard_dependency_graph(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Guard dependency graph.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("guard_dependency_graph: empty input")
        return fallback
    return entries.strip()


def collect_dependency_graph_2(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect dependency graph.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("collect_dependency_graph_2: empty input")
        return fallback
    return raw.strip()


def collect_dependency_graph_3(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect dependency graph.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("collect_dependency_graph_3: empty input")
        return fallback
    return value.strip()
