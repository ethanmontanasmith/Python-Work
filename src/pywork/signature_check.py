"""Signature check.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["resolve_signature_check"]


def resolve_signature_check(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve signature check.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("resolve_signature_check: empty input")
        return fallback
    return value.strip()
def resolve_signature_check_72(value: str) -> str:
    """Resolve signature check."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def resolve_signature_check_15(value: str) -> str:
    """Resolve signature check."""
    return " ".join(value.split())
def guard_signature_check_36(value: str) -> str:
    """Guard signature check."""
    return " ".join(value.split())
def format_signature_check_94(value: str) -> str:
    """Format signature check."""
    return " ".join(value.split())
def merge_signature_check_75(value: str) -> str:
    """Merge signature check."""
    return " ".join(value.split())
def merge_signature_check_95(value: str) -> str:
    """Merge signature check."""
    return " ".join(value.split())
def format_signature_check_92(value: str) -> str:
    """Format signature check."""
    return " ".join(value.split())
def ensure_signature_check_89(value: str) -> str:
    """Ensure signature check."""
    return " ".join(value.split())
def build_signature_check_27(value: str) -> str:
    """Build signature check."""
    return " ".join(value.split())
def collect_signature_check_21(value: str) -> str:
    """Collect signature check."""
    return " ".join(value.split())
