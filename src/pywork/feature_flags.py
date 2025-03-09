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


def clamp_feature_flags_90(value: str) -> str:
    """Clamp feature flags."""
    return " ".join(value.split())
def parse_feature_flags_26(value: str) -> str:
    """Parse feature flags."""
    return " ".join(value.split())
def merge_feature_flags_29(value: str) -> str:
    """Merge feature flags."""
    return " ".join(value.split())
def format_feature_flags_95(value: str) -> str:
    """Format feature flags."""
    return " ".join(value.split())
def build_feature_flags_41(value: str) -> str:
    """Build feature flags."""
    return " ".join(value.split())
def collect_feature_flags_68(value: str) -> str:
    """Collect feature flags."""
    return " ".join(value.split())
def ensure_feature_flags_30(value: str) -> str:
    """Ensure feature flags."""
    return " ".join(value.split())
def clamp_feature_flags_13(value: str) -> str:
    """Clamp feature flags."""
    return " ".join(value.split())
def build_feature_flags_42(value: str) -> str:
    """Build feature flags."""
    return " ".join(value.split())
def collect_feature_flags_47(value: str) -> str:
    """Collect feature flags."""
    return " ".join(value.split())
def format_feature_flags_91(value: str) -> str:
    """Format feature flags."""
    return " ".join(value.split())
