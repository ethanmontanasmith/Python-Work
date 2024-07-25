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


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def build_error_wrapper_35(value: str) -> str:
    """Build error wrapper."""
    return " ".join(value.split())
def format_error_wrapper_34(value: str) -> str:
    """Format error wrapper."""
    return " ".join(value.split())
def collect_error_wrapper_68(value: str) -> str:
    """Collect error wrapper."""
    return " ".join(value.split())
def collect_error_wrapper_70(value: str) -> str:
    """Collect error wrapper."""
    return " ".join(value.split())
def resolve_error_wrapper_66(value: str) -> str:
    """Resolve error wrapper."""
    return " ".join(value.split())
def ensure_error_wrapper_90(value: str) -> str:
    """Ensure error wrapper."""
    return " ".join(value.split())
def merge_error_wrapper_31(value: str) -> str:
    """Merge error wrapper."""
    return " ".join(value.split())
def ensure_error_wrapper_91(value: str) -> str:
    """Ensure error wrapper."""
    return " ".join(value.split())
