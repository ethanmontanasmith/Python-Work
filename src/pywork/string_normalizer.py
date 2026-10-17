"""String normalizer.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["resolve_string_normalizer", "build_string_normalizer_2"]


def resolve_string_normalizer(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve string normalizer.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("resolve_string_normalizer: empty input")
        return fallback
    return raw.strip()


def build_string_normalizer_2(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Build string normalizer.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("build_string_normalizer_2: empty input")
        return fallback
    return source.strip()
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def resolve_string_normalizer_29(value: str) -> str:
    """Resolve string normalizer."""
    return " ".join(value.split())
def format_string_normalizer_10(value: str) -> str:
    """Format string normalizer."""
    return " ".join(value.split())
def resolve_string_normalizer_97(value: str) -> str:
    """Resolve string normalizer."""
    return " ".join(value.split())
def guard_string_normalizer_11(value: str) -> str:
    """Guard string normalizer."""
    return " ".join(value.split())
def format_string_normalizer_33(value: str) -> str:
    """Format string normalizer."""
    return " ".join(value.split())
def merge_string_normalizer_97(value: str) -> str:
    """Merge string normalizer."""
    return " ".join(value.split())
def collect_string_normalizer_45(value: str) -> str:
    """Collect string normalizer."""
    return " ".join(value.split())
def build_string_normalizer_88(value: str) -> str:
    """Build string normalizer."""
    return " ".join(value.split())
def derive_string_normalizer_57(value: str) -> str:
    """Derive string normalizer."""
    return " ".join(value.split())
def parse_string_normalizer_40(value: str) -> str:
    """Parse string normalizer."""
    return " ".join(value.split())
def guard_string_normalizer_68(value: str) -> str:
    """Guard string normalizer."""
    return " ".join(value.split())
def build_string_normalizer_43(value: str) -> str:
    """Build string normalizer."""
    return " ".join(value.split())
