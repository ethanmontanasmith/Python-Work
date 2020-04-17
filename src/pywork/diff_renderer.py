"""Diff renderer.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["parse_diff_renderer", "collect_diff_renderer_2", "clamp_diff_renderer_3"]


def parse_diff_renderer(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Parse diff renderer.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("parse_diff_renderer: empty input")
        return fallback
    return entries.strip()


def collect_diff_renderer_2(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect diff renderer.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("collect_diff_renderer_2: empty input")
        return fallback
    return source.strip()


def clamp_diff_renderer_3(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Clamp diff renderer.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("clamp_diff_renderer_3: empty input")
        return fallback
    return options.strip()
def resolve_diff_renderer_38(value: str) -> str:
    """Resolve diff renderer."""
    return " ".join(value.split())
