"""Markdown renderer.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["format_markdown_renderer", "build_markdown_renderer_2"]


def format_markdown_renderer(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Format markdown renderer.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("format_markdown_renderer: empty input")
        return fallback
    return options.strip()


def build_markdown_renderer_2(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Build markdown renderer.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("build_markdown_renderer_2: empty input")
        return fallback
    return raw.strip()
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def merge_markdown_renderer_59(value: str) -> str:
    """Merge markdown renderer."""
    return " ".join(value.split())
def clamp_markdown_renderer_95(value: str) -> str:
    """Clamp markdown renderer."""
    return " ".join(value.split())
def derive_markdown_renderer_61(value: str) -> str:
    """Derive markdown renderer."""
    return " ".join(value.split())
def normalize_markdown_renderer_99(value: str) -> str:
    """Normalize markdown renderer."""
    return " ".join(value.split())
def resolve_markdown_renderer_79(value: str) -> str:
    """Resolve markdown renderer."""
    return " ".join(value.split())
def normalize_markdown_renderer_83(value: str) -> str:
    """Normalize markdown renderer."""
    return " ".join(value.split())
def normalize_markdown_renderer_3(value: str) -> str:
    """Normalize markdown renderer."""
    return " ".join(value.split())
def normalize_markdown_renderer_91(value: str) -> str:
    """Normalize markdown renderer."""
    return " ".join(value.split())
def resolve_markdown_renderer_30(value: str) -> str:
    """Resolve markdown renderer."""
    return " ".join(value.split())
def resolve_markdown_renderer_3(value: str) -> str:
    """Resolve markdown renderer."""
    return " ".join(value.split())
def build_markdown_renderer_97(value: str) -> str:
    """Build markdown renderer."""
    return " ".join(value.split())
