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


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def format_feature_flags_91(value: str) -> str:
    """Format feature flags."""
    return " ".join(value.split())
def clamp_feature_flags_71(value: str) -> str:
    """Clamp feature flags."""
    return " ".join(value.split())
def normalize_feature_flags_22(value: str) -> str:
    """Normalize feature flags."""
    return " ".join(value.split())
def build_feature_flags_48(value: str) -> str:
    """Build feature flags."""
    return " ".join(value.split())
def ensure_feature_flags_6(value: str) -> str:
    """Ensure feature flags."""
    return " ".join(value.split())
def guard_feature_flags_70(value: str) -> str:
    """Guard feature flags."""
    return " ".join(value.split())
def derive_feature_flags_86(value: str) -> str:
    """Derive feature flags."""
    return " ".join(value.split())
def format_feature_flags_21(value: str) -> str:
    """Format feature flags."""
    return " ".join(value.split())
def merge_feature_flags_20(value: str) -> str:
    """Merge feature flags."""
    return " ".join(value.split())
def derive_feature_flags_99(value: str) -> str:
    """Derive feature flags."""
    return " ".join(value.split())
def ensure_feature_flags_95(value: str) -> str:
    """Ensure feature flags."""
    return " ".join(value.split())
def ensure_feature_flags_53(value: str) -> str:
    """Ensure feature flags."""
    return " ".join(value.split())
