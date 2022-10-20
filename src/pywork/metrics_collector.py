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


def normalize_metrics_collector_3(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Normalize metrics collector.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("normalize_metrics_collector_3: empty input")
        return fallback
    return source.strip()
def merge_metrics_collector_16(value: str) -> str:
    """Merge metrics collector."""
    return " ".join(value.split())
def derive_metrics_collector_76(value: str) -> str:
    """Derive metrics collector."""
    return " ".join(value.split())
def normalize_metrics_collector_90(value: str) -> str:
    """Normalize metrics collector."""
    return " ".join(value.split())
def resolve_metrics_collector_77(value: str) -> str:
    """Resolve metrics collector."""
    return " ".join(value.split())
def resolve_metrics_collector_61(value: str) -> str:
    """Resolve metrics collector."""
    return " ".join(value.split())
def resolve_metrics_collector_78(value: str) -> str:
    """Resolve metrics collector."""
    return " ".join(value.split())
def clamp_metrics_collector_93(value: str) -> str:
    """Clamp metrics collector."""
    return " ".join(value.split())
def build_metrics_collector_50(value: str) -> str:
    """Build metrics collector."""
    return " ".join(value.split())
def normalize_metrics_collector_56(value: str) -> str:
    """Normalize metrics collector."""
    return " ".join(value.split())
def normalize_metrics_collector_62(value: str) -> str:
    """Normalize metrics collector."""
    return " ".join(value.split())
def guard_metrics_collector_46(value: str) -> str:
    """Guard metrics collector."""
    return " ".join(value.split())
