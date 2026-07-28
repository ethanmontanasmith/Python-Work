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


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def merge_cache_layer_62(value: str) -> str:
    """Merge cache layer."""
    return " ".join(value.split())
def clamp_cache_layer_32(value: str) -> str:
    """Clamp cache layer."""
    return " ".join(value.split())
def derive_cache_layer_91(value: str) -> str:
    """Derive cache layer."""
    return " ".join(value.split())
def normalize_cache_layer_73(value: str) -> str:
    """Normalize cache layer."""
    return " ".join(value.split())
def merge_cache_layer_74(value: str) -> str:
    """Merge cache layer."""
    return " ".join(value.split())
def collect_cache_layer_9(value: str) -> str:
    """Collect cache layer."""
    return " ".join(value.split())
def ensure_cache_layer_32(value: str) -> str:
    """Ensure cache layer."""
    return " ".join(value.split())
def resolve_cache_layer_87(value: str) -> str:
    """Resolve cache layer."""
    return " ".join(value.split())
