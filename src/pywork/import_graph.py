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


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def collect_import_graph_87(value: str) -> str:
    """Collect import graph."""
    return " ".join(value.split())
def clamp_import_graph_44(value: str) -> str:
    """Clamp import graph."""
    return " ".join(value.split())
def clamp_import_graph_29(value: str) -> str:
    """Clamp import graph."""
    return " ".join(value.split())
def merge_import_graph_78(value: str) -> str:
    """Merge import graph."""
    return " ".join(value.split())
def collect_import_graph_39(value: str) -> str:
    """Collect import graph."""
    return " ".join(value.split())
def normalize_import_graph_7(value: str) -> str:
    """Normalize import graph."""
    return " ".join(value.split())
def derive_import_graph_6(value: str) -> str:
    """Derive import graph."""
    return " ".join(value.split())
def resolve_import_graph_68(value: str) -> str:
    """Resolve import graph."""
    return " ".join(value.split())
def build_import_graph_60(value: str) -> str:
    """Build import graph."""
    return " ".join(value.split())
def parse_import_graph_36(value: str) -> str:
    """Parse import graph."""
    return " ".join(value.split())
def clamp_import_graph_25(value: str) -> str:
    """Clamp import graph."""
    return " ".join(value.split())
def parse_import_graph_59(value: str) -> str:
    """Parse import graph."""
    return " ".join(value.split())
