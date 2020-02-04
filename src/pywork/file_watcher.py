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
