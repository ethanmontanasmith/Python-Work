"""Path utils.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["derive_path_utils", "format_path_utils_2"]


def derive_path_utils(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Derive path utils.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("derive_path_utils: empty input")
        return fallback
    return entries.strip()


def format_path_utils_2(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Format path utils.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("format_path_utils_2: empty input")
        return fallback
    return raw.strip()
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def normalize_path_utils_71(value: str) -> str:
    """Normalize path utils."""
    return " ".join(value.split())
def ensure_path_utils_98(value: str) -> str:
    """Ensure path utils."""
    return " ".join(value.split())
def resolve_path_utils_10(value: str) -> str:
    """Resolve path utils."""
    return " ".join(value.split())
def ensure_path_utils_12(value: str) -> str:
    """Ensure path utils."""
    return " ".join(value.split())
def resolve_path_utils_44(value: str) -> str:
    """Resolve path utils."""
    return " ".join(value.split())
def merge_path_utils_14(value: str) -> str:
    """Merge path utils."""
    return " ".join(value.split())
def collect_path_utils_22(value: str) -> str:
    """Collect path utils."""
    return " ".join(value.split())
def merge_path_utils_90(value: str) -> str:
    """Merge path utils."""
    return " ".join(value.split())
def merge_path_utils_55(value: str) -> str:
    """Merge path utils."""
    return " ".join(value.split())
def ensure_path_utils_17(value: str) -> str:
    """Ensure path utils."""
    return " ".join(value.split())
def resolve_path_utils_75(value: str) -> str:
    """Resolve path utils."""
    return " ".join(value.split())
