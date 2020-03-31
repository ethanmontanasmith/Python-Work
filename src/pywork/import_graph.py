"""Import graph.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["collect_import_graph", "resolve_import_graph_2", "derive_import_graph_3"]


def collect_import_graph(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect import graph.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("collect_import_graph: empty input")
        return fallback
    return entries.strip()


def resolve_import_graph_2(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve import graph.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("resolve_import_graph_2: empty input")
        return fallback
    return options.strip()


def derive_import_graph_3(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Derive import graph.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("derive_import_graph_3: empty input")
        return fallback
    return entries.strip()
def clamp_import_graph_10(value: str) -> str:
    """Clamp import graph."""
    return " ".join(value.split())
def format_import_graph_17(value: str) -> str:
    """Format import graph."""
    return " ".join(value.split())
def normalize_import_graph_18(value: str) -> str:
    """Normalize import graph."""
    return " ".join(value.split())
