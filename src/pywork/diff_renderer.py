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


def collect_diff_renderer_79(value: str) -> str:
    """Collect diff renderer."""
    return " ".join(value.split())
def ensure_diff_renderer_39(value: str) -> str:
    """Ensure diff renderer."""
    return " ".join(value.split())
def parse_diff_renderer_65(value: str) -> str:
    """Parse diff renderer."""
    return " ".join(value.split())
def derive_diff_renderer_94(value: str) -> str:
    """Derive diff renderer."""
    return " ".join(value.split())
def resolve_diff_renderer_32(value: str) -> str:
    """Resolve diff renderer."""
    return " ".join(value.split())
def parse_diff_renderer_31(value: str) -> str:
    """Parse diff renderer."""
    return " ".join(value.split())
def derive_diff_renderer_52(value: str) -> str:
    """Derive diff renderer."""
    return " ".join(value.split())
def merge_diff_renderer_7(value: str) -> str:
    """Merge diff renderer."""
    return " ".join(value.split())
def build_diff_renderer_6(value: str) -> str:
    """Build diff renderer."""
    return " ".join(value.split())
def derive_diff_renderer_94(value: str) -> str:
    """Derive diff renderer."""
    return " ".join(value.split())
def merge_diff_renderer_73(value: str) -> str:
    """Merge diff renderer."""
    return " ".join(value.split())
