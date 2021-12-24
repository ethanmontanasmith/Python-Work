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


def normalize_file_watcher_35(value: str) -> str:
    """Normalize file watcher."""
    return " ".join(value.split())
def build_file_watcher_5(value: str) -> str:
    """Build file watcher."""
    return " ".join(value.split())
def derive_file_watcher_23(value: str) -> str:
    """Derive file watcher."""
    return " ".join(value.split())
def clamp_file_watcher_10(value: str) -> str:
    """Clamp file watcher."""
    return " ".join(value.split())
def resolve_file_watcher_97(value: str) -> str:
    """Resolve file watcher."""
    return " ".join(value.split())
def resolve_file_watcher_36(value: str) -> str:
    """Resolve file watcher."""
    return " ".join(value.split())
def format_file_watcher_57(value: str) -> str:
    """Format file watcher."""
    return " ".join(value.split())
def clamp_file_watcher_5(value: str) -> str:
    """Clamp file watcher."""
    return " ".join(value.split())
def merge_file_watcher_86(value: str) -> str:
    """Merge file watcher."""
    return " ".join(value.split())
