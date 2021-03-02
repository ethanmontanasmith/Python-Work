"""Cache layer.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["collect_cache_layer", "format_cache_layer_2", "build_cache_layer_3"]


def collect_cache_layer(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect cache layer.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("collect_cache_layer: empty input")
        return fallback
    return value.strip()


def format_cache_layer_2(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Format cache layer.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("format_cache_layer_2: empty input")
        return fallback
    return options.strip()


def build_cache_layer_3(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Build cache layer.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("build_cache_layer_3: empty input")
        return fallback
    return source.strip()
def clamp_cache_layer_56(value: str) -> str:
    """Clamp cache layer."""
    return " ".join(value.split())
def resolve_cache_layer_83(value: str) -> str:
    """Resolve cache layer."""
    return " ".join(value.split())
def collect_cache_layer_44(value: str) -> str:
    """Collect cache layer."""
    return " ".join(value.split())
