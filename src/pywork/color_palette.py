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
