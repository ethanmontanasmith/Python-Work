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
def resolve_feature_flags_66(value: str) -> str:
    """Resolve feature flags."""
    return " ".join(value.split())
def ensure_feature_flags_18(value: str) -> str:
    """Ensure feature flags."""
    return " ".join(value.split())
def build_feature_flags_67(value: str) -> str:
    """Build feature flags."""
    return " ".join(value.split())
def normalize_feature_flags_12(value: str) -> str:
    """Normalize feature flags."""
    return " ".join(value.split())
