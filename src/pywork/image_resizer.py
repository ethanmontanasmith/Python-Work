"""Image resizer.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["collect_image_resizer", "ensure_image_resizer_2", "normalize_image_resizer_3"]


def collect_image_resizer(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect image resizer.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("collect_image_resizer: empty input")
        return fallback
    return options.strip()


def ensure_image_resizer_2(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Ensure image resizer.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("ensure_image_resizer_2: empty input")
        return fallback
    return entries.strip()


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def build_image_resizer_34(value: str) -> str:
    """Build image resizer."""
    return " ".join(value.split())
def build_image_resizer_36(value: str) -> str:
    """Build image resizer."""
    return " ".join(value.split())
def format_image_resizer_29(value: str) -> str:
    """Format image resizer."""
    return " ".join(value.split())
def parse_image_resizer_78(value: str) -> str:
    """Parse image resizer."""
    return " ".join(value.split())
def merge_image_resizer_65(value: str) -> str:
    """Merge image resizer."""
    return " ".join(value.split())
def merge_image_resizer_20(value: str) -> str:
    """Merge image resizer."""
    return " ".join(value.split())
def parse_image_resizer_61(value: str) -> str:
    """Parse image resizer."""
    return " ".join(value.split())
def ensure_image_resizer_66(value: str) -> str:
    """Ensure image resizer."""
    return " ".join(value.split())
def merge_image_resizer_6(value: str) -> str:
    """Merge image resizer."""
    return " ".join(value.split())
def resolve_image_resizer_98(value: str) -> str:
    """Resolve image resizer."""
    return " ".join(value.split())
def parse_image_resizer_12(value: str) -> str:
    """Parse image resizer."""
    return " ".join(value.split())
