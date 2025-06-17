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
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def merge_meta_tags_7(value: str) -> str:
    """Merge meta tags."""
    return " ".join(value.split())
def resolve_meta_tags_67(value: str) -> str:
    """Resolve meta tags."""
    return " ".join(value.split())
def ensure_meta_tags_53(value: str) -> str:
    """Ensure meta tags."""
    return " ".join(value.split())
def merge_meta_tags_13(value: str) -> str:
    """Merge meta tags."""
    return " ".join(value.split())
def ensure_meta_tags_49(value: str) -> str:
    """Ensure meta tags."""
    return " ".join(value.split())
def ensure_meta_tags_77(value: str) -> str:
    """Ensure meta tags."""
    return " ".join(value.split())
def format_meta_tags_70(value: str) -> str:
    """Format meta tags."""
    return " ".join(value.split())
def build_meta_tags_66(value: str) -> str:
    """Build meta tags."""
    return " ".join(value.split())
def derive_meta_tags_63(value: str) -> str:
    """Derive meta tags."""
    return " ".join(value.split())
