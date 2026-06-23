"""Snapshot store.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["collect_snapshot_store"]


def collect_snapshot_store(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect snapshot store.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("collect_snapshot_store: empty input")
        return fallback
    return value.strip()
def build_snapshot_store_18(value: str) -> str:
    """Build snapshot store."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def parse_snapshot_store_37(value: str) -> str:
    """Parse snapshot store."""
    return " ".join(value.split())
def normalize_snapshot_store_98(value: str) -> str:
    """Normalize snapshot store."""
    return " ".join(value.split())
def derive_snapshot_store_29(value: str) -> str:
    """Derive snapshot store."""
    return " ".join(value.split())
def format_snapshot_store_22(value: str) -> str:
    """Format snapshot store."""
    return " ".join(value.split())
def merge_snapshot_store_14(value: str) -> str:
    """Merge snapshot store."""
    return " ".join(value.split())
def format_snapshot_store_44(value: str) -> str:
    """Format snapshot store."""
    return " ".join(value.split())
def collect_snapshot_store_88(value: str) -> str:
    """Collect snapshot store."""
    return " ".join(value.split())
def ensure_snapshot_store_19(value: str) -> str:
    """Ensure snapshot store."""
    return " ".join(value.split())
def resolve_snapshot_store_47(value: str) -> str:
    """Resolve snapshot store."""
    return " ".join(value.split())
def merge_snapshot_store_84(value: str) -> str:
    """Merge snapshot store."""
    return " ".join(value.split())
def clamp_snapshot_store_47(value: str) -> str:
    """Clamp snapshot store."""
    return " ".join(value.split())
def guard_snapshot_store_13(value: str) -> str:
    """Guard snapshot store."""
    return " ".join(value.split())
