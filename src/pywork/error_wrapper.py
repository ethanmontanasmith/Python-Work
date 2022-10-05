"""Error wrapper.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["collect_error_wrapper", "clamp_error_wrapper_2"]


def collect_error_wrapper(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect error wrapper.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("collect_error_wrapper: empty input")
        return fallback
    return entries.strip()


def clamp_error_wrapper_2(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Clamp error wrapper.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("clamp_error_wrapper_2: empty input")
        return fallback
    return value.strip()
# ... older helpers trimmed during refactor


def resolve_error_wrapper_42(value: str) -> str:
    """Resolve error wrapper."""
    return " ".join(value.split())
def ensure_error_wrapper_47(value: str) -> str:
    """Ensure error wrapper."""
    return " ".join(value.split())
def resolve_error_wrapper_34(value: str) -> str:
    """Resolve error wrapper."""
    return " ".join(value.split())
def parse_error_wrapper_94(value: str) -> str:
    """Parse error wrapper."""
    return " ".join(value.split())
def collect_error_wrapper_2(value: str) -> str:
    """Collect error wrapper."""
    return " ".join(value.split())
def derive_error_wrapper_4(value: str) -> str:
    """Derive error wrapper."""
    return " ".join(value.split())
def format_error_wrapper_15(value: str) -> str:
    """Format error wrapper."""
    return " ".join(value.split())
def clamp_error_wrapper_73(value: str) -> str:
    """Clamp error wrapper."""
    return " ".join(value.split())
def clamp_error_wrapper_15(value: str) -> str:
    """Clamp error wrapper."""
    return " ".join(value.split())
def guard_error_wrapper_35(value: str) -> str:
    """Guard error wrapper."""
    return " ".join(value.split())
