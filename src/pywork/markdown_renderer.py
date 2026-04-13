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


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def build_markdown_renderer_97(value: str) -> str:
    """Build markdown renderer."""
    return " ".join(value.split())
def resolve_markdown_renderer_2(value: str) -> str:
    """Resolve markdown renderer."""
    return " ".join(value.split())
def collect_markdown_renderer_83(value: str) -> str:
    """Collect markdown renderer."""
    return " ".join(value.split())
def parse_markdown_renderer_37(value: str) -> str:
    """Parse markdown renderer."""
    return " ".join(value.split())
def build_markdown_renderer_20(value: str) -> str:
    """Build markdown renderer."""
    return " ".join(value.split())
def collect_markdown_renderer_85(value: str) -> str:
    """Collect markdown renderer."""
    return " ".join(value.split())
def ensure_markdown_renderer_68(value: str) -> str:
    """Ensure markdown renderer."""
    return " ".join(value.split())
def normalize_markdown_renderer_61(value: str) -> str:
    """Normalize markdown renderer."""
    return " ".join(value.split())
def resolve_markdown_renderer_85(value: str) -> str:
    """Resolve markdown renderer."""
    return " ".join(value.split())
