"""Date helpers.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["build_date_helpers", "collect_date_helpers_2"]


def build_date_helpers(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Build date helpers.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("build_date_helpers: empty input")
        return fallback
    return raw.strip()


def collect_date_helpers_2(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect date helpers.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("collect_date_helpers_2: empty input")
        return fallback
    return options.strip()
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def parse_date_helpers_95(value: str) -> str:
    """Parse date helpers."""
    return " ".join(value.split())
def merge_date_helpers_33(value: str) -> str:
    """Merge date helpers."""
    return " ".join(value.split())
def resolve_date_helpers_75(value: str) -> str:
    """Resolve date helpers."""
    return " ".join(value.split())
def merge_date_helpers_16(value: str) -> str:
    """Merge date helpers."""
    return " ".join(value.split())
def merge_date_helpers_46(value: str) -> str:
    """Merge date helpers."""
    return " ".join(value.split())
def collect_date_helpers_30(value: str) -> str:
    """Collect date helpers."""
    return " ".join(value.split())
def merge_date_helpers_26(value: str) -> str:
    """Merge date helpers."""
    return " ".join(value.split())
def ensure_date_helpers_81(value: str) -> str:
    """Ensure date helpers."""
    return " ".join(value.split())
def merge_date_helpers_47(value: str) -> str:
    """Merge date helpers."""
    return " ".join(value.split())
