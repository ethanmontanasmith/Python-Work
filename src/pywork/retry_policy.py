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


def guard_retry_policy_3(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Guard retry policy.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("guard_retry_policy_3: empty input")
        return fallback
    return value.strip()
def guard_retry_policy_9(value: str) -> str:
    """Guard retry policy."""
    return " ".join(value.split())
def ensure_retry_policy_20(value: str) -> str:
    """Ensure retry policy."""
    return " ".join(value.split())
