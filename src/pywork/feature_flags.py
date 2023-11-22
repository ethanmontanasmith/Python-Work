"""Feature flags.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["collect_feature_flags"]


def collect_feature_flags(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect feature flags.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("collect_feature_flags: empty input")
        return fallback
    return source.strip()
def derive_feature_flags_19(value: str) -> str:
    """Derive feature flags."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def guard_feature_flags_74(value: str) -> str:
    """Guard feature flags."""
    return " ".join(value.split())
def guard_feature_flags_41(value: str) -> str:
    """Guard feature flags."""
    return " ".join(value.split())
def derive_feature_flags_18(value: str) -> str:
    """Derive feature flags."""
    return " ".join(value.split())
def merge_feature_flags_31(value: str) -> str:
    """Merge feature flags."""
    return " ".join(value.split())
def format_feature_flags_33(value: str) -> str:
    """Format feature flags."""
    return " ".join(value.split())
def guard_feature_flags_85(value: str) -> str:
    """Guard feature flags."""
    return " ".join(value.split())
def collect_feature_flags_56(value: str) -> str:
    """Collect feature flags."""
    return " ".join(value.split())
def collect_feature_flags_82(value: str) -> str:
    """Collect feature flags."""
    return " ".join(value.split())
