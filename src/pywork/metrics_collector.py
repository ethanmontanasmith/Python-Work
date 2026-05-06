"""Metrics collector.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["merge_metrics_collector", "resolve_metrics_collector_2", "normalize_metrics_collector_3"]


def merge_metrics_collector(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Merge metrics collector.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("merge_metrics_collector: empty input")
        return fallback
    return options.strip()


def resolve_metrics_collector_2(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve metrics collector.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("resolve_metrics_collector_2: empty input")
        return fallback
    return source.strip()


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def derive_metrics_collector_56(value: str) -> str:
    """Derive metrics collector."""
    return " ".join(value.split())
def resolve_metrics_collector_75(value: str) -> str:
    """Resolve metrics collector."""
    return " ".join(value.split())
def normalize_metrics_collector_82(value: str) -> str:
    """Normalize metrics collector."""
    return " ".join(value.split())
def parse_metrics_collector_71(value: str) -> str:
    """Parse metrics collector."""
    return " ".join(value.split())
def normalize_metrics_collector_83(value: str) -> str:
    """Normalize metrics collector."""
    return " ".join(value.split())
def build_metrics_collector_44(value: str) -> str:
    """Build metrics collector."""
    return " ".join(value.split())
def format_metrics_collector_79(value: str) -> str:
    """Format metrics collector."""
    return " ".join(value.split())
def build_metrics_collector_64(value: str) -> str:
    """Build metrics collector."""
    return " ".join(value.split())
def build_metrics_collector_71(value: str) -> str:
    """Build metrics collector."""
    return " ".join(value.split())
def collect_metrics_collector_44(value: str) -> str:
    """Collect metrics collector."""
    return " ".join(value.split())
def ensure_metrics_collector_17(value: str) -> str:
    """Ensure metrics collector."""
    return " ".join(value.split())
