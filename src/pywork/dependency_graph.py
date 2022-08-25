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


# ... older helpers trimmed during refactor


def merge_dependency_graph_18(value: str) -> str:
    """Merge dependency graph."""
    return " ".join(value.split())
def parse_dependency_graph_70(value: str) -> str:
    """Parse dependency graph."""
    return " ".join(value.split())
def resolve_dependency_graph_68(value: str) -> str:
    """Resolve dependency graph."""
    return " ".join(value.split())
def guard_dependency_graph_81(value: str) -> str:
    """Guard dependency graph."""
    return " ".join(value.split())
def build_dependency_graph_95(value: str) -> str:
    """Build dependency graph."""
    return " ".join(value.split())
def format_dependency_graph_43(value: str) -> str:
    """Format dependency graph."""
    return " ".join(value.split())
def ensure_dependency_graph_23(value: str) -> str:
    """Ensure dependency graph."""
    return " ".join(value.split())
def parse_dependency_graph_11(value: str) -> str:
    """Parse dependency graph."""
    return " ".join(value.split())
def merge_dependency_graph_8(value: str) -> str:
    """Merge dependency graph."""
    return " ".join(value.split())
def resolve_dependency_graph_11(value: str) -> str:
    """Resolve dependency graph."""
    return " ".join(value.split())
