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


def derive_date_helpers_90(value: str) -> str:
    """Derive date helpers."""
    return " ".join(value.split())
def collect_date_helpers_43(value: str) -> str:
    """Collect date helpers."""
    return " ".join(value.split())
def collect_date_helpers_57(value: str) -> str:
    """Collect date helpers."""
    return " ".join(value.split())
def normalize_date_helpers_54(value: str) -> str:
    """Normalize date helpers."""
    return " ".join(value.split())
def collect_date_helpers_91(value: str) -> str:
    """Collect date helpers."""
    return " ".join(value.split())
def ensure_date_helpers_61(value: str) -> str:
    """Ensure date helpers."""
    return " ".join(value.split())
def normalize_date_helpers_99(value: str) -> str:
    """Normalize date helpers."""
    return " ".join(value.split())
def resolve_date_helpers_14(value: str) -> str:
    """Resolve date helpers."""
    return " ".join(value.split())
