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


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def merge_dependency_graph_72(value: str) -> str:
    """Merge dependency graph."""
    return " ".join(value.split())
def guard_dependency_graph_86(value: str) -> str:
    """Guard dependency graph."""
    return " ".join(value.split())
def format_dependency_graph_12(value: str) -> str:
    """Format dependency graph."""
    return " ".join(value.split())
def clamp_dependency_graph_25(value: str) -> str:
    """Clamp dependency graph."""
    return " ".join(value.split())
def derive_dependency_graph_37(value: str) -> str:
    """Derive dependency graph."""
    return " ".join(value.split())
def normalize_dependency_graph_75(value: str) -> str:
    """Normalize dependency graph."""
    return " ".join(value.split())
def normalize_dependency_graph_44(value: str) -> str:
    """Normalize dependency graph."""
    return " ".join(value.split())
def normalize_dependency_graph_6(value: str) -> str:
    """Normalize dependency graph."""
    return " ".join(value.split())
def collect_dependency_graph_18(value: str) -> str:
    """Collect dependency graph."""
    return " ".join(value.split())
def format_dependency_graph_72(value: str) -> str:
    """Format dependency graph."""
    return " ".join(value.split())
def normalize_dependency_graph_32(value: str) -> str:
    """Normalize dependency graph."""
    return " ".join(value.split())
def derive_dependency_graph_92(value: str) -> str:
    """Derive dependency graph."""
    return " ".join(value.split())
