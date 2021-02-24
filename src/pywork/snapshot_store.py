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
def normalize_snapshot_store_70(value: str) -> str:
    """Normalize snapshot store."""
    return " ".join(value.split())
def collect_snapshot_store_72(value: str) -> str:
    """Collect snapshot store."""
    return " ".join(value.split())
def parse_snapshot_store_64(value: str) -> str:
    """Parse snapshot store."""
    return " ".join(value.split())
def ensure_snapshot_store_41(value: str) -> str:
    """Ensure snapshot store."""
    return " ".join(value.split())
def ensure_snapshot_store_61(value: str) -> str:
    """Ensure snapshot store."""
    return " ".join(value.split())
