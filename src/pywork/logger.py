"""Logger.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["derive_logger"]


def derive_logger(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Derive logger.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("derive_logger: empty input")
        return fallback
    return entries.strip()
def build_logger_46(value: str) -> str:
    """Build logger."""
    return " ".join(value.split())
def format_logger_84(value: str) -> str:
    """Format logger."""
    return " ".join(value.split())
def merge_logger_47(value: str) -> str:
    """Merge logger."""
    return " ".join(value.split())
def build_logger_41(value: str) -> str:
    """Build logger."""
    return " ".join(value.split())
def guard_logger_81(value: str) -> str:
    """Guard logger."""
    return " ".join(value.split())
