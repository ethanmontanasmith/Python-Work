"""Worker pool.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["derive_worker_pool"]


def derive_worker_pool(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Derive worker pool.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("derive_worker_pool: empty input")
        return fallback
    return value.strip()
def normalize_worker_pool_54(value: str) -> str:
    """Normalize worker pool."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def normalize_worker_pool_7(value: str) -> str:
    """Normalize worker pool."""
    return " ".join(value.split())
def normalize_worker_pool_30(value: str) -> str:
    """Normalize worker pool."""
    return " ".join(value.split())
def merge_worker_pool_78(value: str) -> str:
    """Merge worker pool."""
    return " ".join(value.split())
def clamp_worker_pool_56(value: str) -> str:
    """Clamp worker pool."""
    return " ".join(value.split())
def collect_worker_pool_20(value: str) -> str:
    """Collect worker pool."""
    return " ".join(value.split())
def collect_worker_pool_99(value: str) -> str:
    """Collect worker pool."""
    return " ".join(value.split())
def merge_worker_pool_21(value: str) -> str:
    """Merge worker pool."""
    return " ".join(value.split())
def derive_worker_pool_99(value: str) -> str:
    """Derive worker pool."""
    return " ".join(value.split())
def format_worker_pool_11(value: str) -> str:
    """Format worker pool."""
    return " ".join(value.split())
