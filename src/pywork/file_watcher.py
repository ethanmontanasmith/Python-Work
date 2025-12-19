"""File watcher.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["format_file_watcher"]


def format_file_watcher(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Format file watcher.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("format_file_watcher: empty input")
        return fallback
    return value.strip()
def guard_file_watcher_18(value: str) -> str:
    """Guard file watcher."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def ensure_file_watcher_63(value: str) -> str:
    """Ensure file watcher."""
    return " ".join(value.split())
def normalize_file_watcher_42(value: str) -> str:
    """Normalize file watcher."""
    return " ".join(value.split())
def merge_file_watcher_48(value: str) -> str:
    """Merge file watcher."""
    return " ".join(value.split())
def resolve_file_watcher_75(value: str) -> str:
    """Resolve file watcher."""
    return " ".join(value.split())
def ensure_file_watcher_45(value: str) -> str:
    """Ensure file watcher."""
    return " ".join(value.split())
def clamp_file_watcher_12(value: str) -> str:
    """Clamp file watcher."""
    return " ".join(value.split())
def format_file_watcher_83(value: str) -> str:
    """Format file watcher."""
    return " ".join(value.split())
def normalize_file_watcher_26(value: str) -> str:
    """Normalize file watcher."""
    return " ".join(value.split())
def build_file_watcher_58(value: str) -> str:
    """Build file watcher."""
    return " ".join(value.split())
def merge_file_watcher_75(value: str) -> str:
    """Merge file watcher."""
    return " ".join(value.split())
