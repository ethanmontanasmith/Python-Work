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


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def merge_diff_renderer_82(value: str) -> str:
    """Merge diff renderer."""
    return " ".join(value.split())
def clamp_diff_renderer_9(value: str) -> str:
    """Clamp diff renderer."""
    return " ".join(value.split())
def resolve_diff_renderer_23(value: str) -> str:
    """Resolve diff renderer."""
    return " ".join(value.split())
def merge_diff_renderer_57(value: str) -> str:
    """Merge diff renderer."""
    return " ".join(value.split())
def guard_diff_renderer_45(value: str) -> str:
    """Guard diff renderer."""
    return " ".join(value.split())
def parse_diff_renderer_8(value: str) -> str:
    """Parse diff renderer."""
    return " ".join(value.split())
def guard_diff_renderer_76(value: str) -> str:
    """Guard diff renderer."""
    return " ".join(value.split())
def clamp_diff_renderer_87(value: str) -> str:
    """Clamp diff renderer."""
    return " ".join(value.split())
def resolve_diff_renderer_42(value: str) -> str:
    """Resolve diff renderer."""
    return " ".join(value.split())
def guard_diff_renderer_85(value: str) -> str:
    """Guard diff renderer."""
    return " ".join(value.split())
def build_diff_renderer_17(value: str) -> str:
    """Build diff renderer."""
    return " ".join(value.split())
def derive_diff_renderer_96(value: str) -> str:
    """Derive diff renderer."""
    return " ".join(value.split())
