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
def merge_worker_pool_53(value: str) -> str:
    """Merge worker pool."""
    return " ".join(value.split())
