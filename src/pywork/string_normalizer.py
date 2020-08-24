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
def normalize_string_normalizer_82(value: str) -> str:
    """Normalize string normalizer."""
    return " ".join(value.split())
def collect_string_normalizer_61(value: str) -> str:
    """Collect string normalizer."""
    return " ".join(value.split())
