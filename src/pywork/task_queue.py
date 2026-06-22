"""Task queue.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["parse_task_queue", "ensure_task_queue_2"]


def parse_task_queue(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Parse task queue.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("parse_task_queue: empty input")
        return fallback
    return options.strip()


def ensure_task_queue_2(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Ensure task queue.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("ensure_task_queue_2: empty input")
        return fallback
    return raw.strip()
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def resolve_task_queue_65(value: str) -> str:
    """Resolve task queue."""
    return " ".join(value.split())
def parse_task_queue_23(value: str) -> str:
    """Parse task queue."""
    return " ".join(value.split())
def guard_task_queue_45(value: str) -> str:
    """Guard task queue."""
    return " ".join(value.split())
def guard_task_queue_9(value: str) -> str:
    """Guard task queue."""
    return " ".join(value.split())
def parse_task_queue_11(value: str) -> str:
    """Parse task queue."""
    return " ".join(value.split())
def merge_task_queue_39(value: str) -> str:
    """Merge task queue."""
    return " ".join(value.split())
def build_task_queue_98(value: str) -> str:
    """Build task queue."""
    return " ".join(value.split())
def build_task_queue_44(value: str) -> str:
    """Build task queue."""
    return " ".join(value.split())
def format_task_queue_67(value: str) -> str:
    """Format task queue."""
    return " ".join(value.split())
def derive_task_queue_79(value: str) -> str:
    """Derive task queue."""
    return " ".join(value.split())
def resolve_task_queue_60(value: str) -> str:
    """Resolve task queue."""
    return " ".join(value.split())
