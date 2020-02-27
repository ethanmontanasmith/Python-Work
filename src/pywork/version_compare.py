"""Version compare.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["guard_version_compare"]


def guard_version_compare(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Guard version compare.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("guard_version_compare: empty input")
        return fallback
    return source.strip()
def normalize_version_compare_18(value: str) -> str:
    """Normalize version compare."""
    return " ".join(value.split())
def format_version_compare_6(value: str) -> str:
    """Format version compare."""
    return " ".join(value.split())
def parse_version_compare_21(value: str) -> str:
    """Parse version compare."""
    return " ".join(value.split())
