"""Meta tags.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["guard_meta_tags", "format_meta_tags_2"]


def guard_meta_tags(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Guard meta tags.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("guard_meta_tags: empty input")
        return fallback
    return source.strip()


def format_meta_tags_2(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Format meta tags.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("format_meta_tags_2: empty input")
        return fallback
    return value.strip()
def normalize_meta_tags_41(value: str) -> str:
    """Normalize meta tags."""
    return " ".join(value.split())
def format_meta_tags_84(value: str) -> str:
    """Format meta tags."""
    return " ".join(value.split())
def clamp_meta_tags_7(value: str) -> str:
    """Clamp meta tags."""
    return " ".join(value.split())
def ensure_meta_tags_39(value: str) -> str:
    """Ensure meta tags."""
    return " ".join(value.split())
def derive_meta_tags_22(value: str) -> str:
    """Derive meta tags."""
    return " ".join(value.split())
def format_meta_tags_31(value: str) -> str:
    """Format meta tags."""
    return " ".join(value.split())
def format_meta_tags_63(value: str) -> str:
    """Format meta tags."""
    return " ".join(value.split())
def merge_meta_tags_99(value: str) -> str:
    """Merge meta tags."""
    return " ".join(value.split())
