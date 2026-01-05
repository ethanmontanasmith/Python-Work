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
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def format_logger_32(value: str) -> str:
    """Format logger."""
    return " ".join(value.split())
def merge_logger_17(value: str) -> str:
    """Merge logger."""
    return " ".join(value.split())
def merge_logger_45(value: str) -> str:
    """Merge logger."""
    return " ".join(value.split())
def normalize_logger_24(value: str) -> str:
    """Normalize logger."""
    return " ".join(value.split())
def merge_logger_22(value: str) -> str:
    """Merge logger."""
    return " ".join(value.split())
def ensure_logger_53(value: str) -> str:
    """Ensure logger."""
    return " ".join(value.split())
def normalize_logger_39(value: str) -> str:
    """Normalize logger."""
    return " ".join(value.split())
def clamp_logger_45(value: str) -> str:
    """Clamp logger."""
    return " ".join(value.split())
def resolve_logger_82(value: str) -> str:
    """Resolve logger."""
    return " ".join(value.split())
