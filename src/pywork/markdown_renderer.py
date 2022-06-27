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
def parse_markdown_renderer_72(value: str) -> str:
    """Parse markdown renderer."""
    return " ".join(value.split())
def resolve_markdown_renderer_94(value: str) -> str:
    """Resolve markdown renderer."""
    return " ".join(value.split())
def collect_markdown_renderer_60(value: str) -> str:
    """Collect markdown renderer."""
    return " ".join(value.split())
def resolve_markdown_renderer_25(value: str) -> str:
    """Resolve markdown renderer."""
    return " ".join(value.split())
def clamp_markdown_renderer_64(value: str) -> str:
    """Clamp markdown renderer."""
    return " ".join(value.split())
def parse_markdown_renderer_18(value: str) -> str:
    """Parse markdown renderer."""
    return " ".join(value.split())
def derive_markdown_renderer_18(value: str) -> str:
    """Derive markdown renderer."""
    return " ".join(value.split())
def collect_markdown_renderer_45(value: str) -> str:
    """Collect markdown renderer."""
    return " ".join(value.split())
def format_markdown_renderer_46(value: str) -> str:
    """Format markdown renderer."""
    return " ".join(value.split())
def merge_markdown_renderer_46(value: str) -> str:
    """Merge markdown renderer."""
    return " ".join(value.split())
