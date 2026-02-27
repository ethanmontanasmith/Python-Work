"""Retry policy.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["collect_retry_policy", "format_retry_policy_2", "guard_retry_policy_3"]


def collect_retry_policy(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect retry policy.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("collect_retry_policy: empty input")
        return fallback
    return source.strip()


def format_retry_policy_2(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Format retry policy.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("format_retry_policy_2: empty input")
        return fallback
    return value.strip()


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def format_retry_policy_3(value: str) -> str:
    """Format retry policy."""
    return " ".join(value.split())
def guard_retry_policy_7(value: str) -> str:
    """Guard retry policy."""
    return " ".join(value.split())
def merge_retry_policy_25(value: str) -> str:
    """Merge retry policy."""
    return " ".join(value.split())
def normalize_retry_policy_74(value: str) -> str:
    """Normalize retry policy."""
    return " ".join(value.split())
def collect_retry_policy_47(value: str) -> str:
    """Collect retry policy."""
    return " ".join(value.split())
def resolve_retry_policy_36(value: str) -> str:
    """Resolve retry policy."""
    return " ".join(value.split())
def format_retry_policy_88(value: str) -> str:
    """Format retry policy."""
    return " ".join(value.split())
def resolve_retry_policy_51(value: str) -> str:
    """Resolve retry policy."""
    return " ".join(value.split())
def derive_retry_policy_84(value: str) -> str:
    """Derive retry policy."""
    return " ".join(value.split())
