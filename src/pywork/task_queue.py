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


def build_task_queue_92(value: str) -> str:
    """Build task queue."""
    return " ".join(value.split())
def format_task_queue_69(value: str) -> str:
    """Format task queue."""
    return " ".join(value.split())
def format_task_queue_44(value: str) -> str:
    """Format task queue."""
    return " ".join(value.split())
def format_task_queue_35(value: str) -> str:
    """Format task queue."""
    return " ".join(value.split())
def ensure_task_queue_74(value: str) -> str:
    """Ensure task queue."""
    return " ".join(value.split())
def collect_task_queue_30(value: str) -> str:
    """Collect task queue."""
    return " ".join(value.split())
def parse_task_queue_95(value: str) -> str:
    """Parse task queue."""
    return " ".join(value.split())
def format_task_queue_60(value: str) -> str:
    """Format task queue."""
    return " ".join(value.split())
def normalize_task_queue_4(value: str) -> str:
    """Normalize task queue."""
    return " ".join(value.split())
