"""Sitemap builder.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["clamp_sitemap_builder", "guard_sitemap_builder_2", "resolve_sitemap_builder_3"]


def clamp_sitemap_builder(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Clamp sitemap builder.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("clamp_sitemap_builder: empty input")
        return fallback
    return options.strip()


def guard_sitemap_builder_2(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Guard sitemap builder.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("guard_sitemap_builder_2: empty input")
        return fallback
    return source.strip()


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def merge_sitemap_builder_41(value: str) -> str:
    """Merge sitemap builder."""
    return " ".join(value.split())
def guard_sitemap_builder_81(value: str) -> str:
    """Guard sitemap builder."""
    return " ".join(value.split())
def clamp_sitemap_builder_14(value: str) -> str:
    """Clamp sitemap builder."""
    return " ".join(value.split())
def guard_sitemap_builder_96(value: str) -> str:
    """Guard sitemap builder."""
    return " ".join(value.split())
def collect_sitemap_builder_50(value: str) -> str:
    """Collect sitemap builder."""
    return " ".join(value.split())
def ensure_sitemap_builder_30(value: str) -> str:
    """Ensure sitemap builder."""
    return " ".join(value.split())
def ensure_sitemap_builder_54(value: str) -> str:
    """Ensure sitemap builder."""
    return " ".join(value.split())
def ensure_sitemap_builder_14(value: str) -> str:
    """Ensure sitemap builder."""
    return " ".join(value.split())
