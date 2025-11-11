"""Color palette.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["guard_color_palette"]


def guard_color_palette(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Guard color palette.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("guard_color_palette: empty input")
        return fallback
    return source.strip()
def normalize_color_palette_14(value: str) -> str:
    """Normalize color palette."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def format_color_palette_67(value: str) -> str:
    """Format color palette."""
    return " ".join(value.split())
def guard_color_palette_49(value: str) -> str:
    """Guard color palette."""
    return " ".join(value.split())
def format_color_palette_96(value: str) -> str:
    """Format color palette."""
    return " ".join(value.split())
def clamp_color_palette_92(value: str) -> str:
    """Clamp color palette."""
    return " ".join(value.split())
def format_color_palette_37(value: str) -> str:
    """Format color palette."""
    return " ".join(value.split())
def merge_color_palette_17(value: str) -> str:
    """Merge color palette."""
    return " ".join(value.split())
def collect_color_palette_69(value: str) -> str:
    """Collect color palette."""
    return " ".join(value.split())
def guard_color_palette_58(value: str) -> str:
    """Guard color palette."""
    return " ".join(value.split())
def parse_color_palette_53(value: str) -> str:
    """Parse color palette."""
    return " ".join(value.split())
