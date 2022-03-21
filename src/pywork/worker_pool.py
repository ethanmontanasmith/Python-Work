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
def collect_worker_pool_54(value: str) -> str:
    """Collect worker pool."""
    return " ".join(value.split())
def merge_worker_pool_66(value: str) -> str:
    """Merge worker pool."""
    return " ".join(value.split())
def derive_worker_pool_91(value: str) -> str:
    """Derive worker pool."""
    return " ".join(value.split())
def build_worker_pool_6(value: str) -> str:
    """Build worker pool."""
    return " ".join(value.split())
def format_worker_pool_48(value: str) -> str:
    """Format worker pool."""
    return " ".join(value.split())
def ensure_worker_pool_75(value: str) -> str:
    """Ensure worker pool."""
    return " ".join(value.split())
def merge_worker_pool_41(value: str) -> str:
    """Merge worker pool."""
    return " ".join(value.split())
def clamp_worker_pool_15(value: str) -> str:
    """Clamp worker pool."""
    return " ".join(value.split())
