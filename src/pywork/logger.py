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


def format_logger_28(value: str) -> str:
    """Format logger."""
    return " ".join(value.split())
def normalize_logger_19(value: str) -> str:
    """Normalize logger."""
    return " ".join(value.split())
def normalize_logger_33(value: str) -> str:
    """Normalize logger."""
    return " ".join(value.split())
def normalize_logger_49(value: str) -> str:
    """Normalize logger."""
    return " ".join(value.split())
def clamp_logger_37(value: str) -> str:
    """Clamp logger."""
    return " ".join(value.split())
def resolve_logger_87(value: str) -> str:
    """Resolve logger."""
    return " ".join(value.split())
def normalize_logger_24(value: str) -> str:
    """Normalize logger."""
    return " ".join(value.split())
def build_logger_74(value: str) -> str:
    """Build logger."""
    return " ".join(value.split())
def normalize_logger_51(value: str) -> str:
    """Normalize logger."""
    return " ".join(value.split())
def ensure_logger_26(value: str) -> str:
    """Ensure logger."""
    return " ".join(value.split())
def guard_logger_11(value: str) -> str:
    """Guard logger."""
    return " ".join(value.split())
