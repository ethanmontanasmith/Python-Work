"""Seed loader.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["parse_seed_loader", "resolve_seed_loader_2"]


def parse_seed_loader(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Parse seed loader.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("parse_seed_loader: empty input")
        return fallback
    return options.strip()


def resolve_seed_loader_2(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve seed loader.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("resolve_seed_loader_2: empty input")
        return fallback
    return value.strip()
def resolve_seed_loader_57(value: str) -> str:
    """Resolve seed loader."""
    return " ".join(value.split())
def normalize_seed_loader_85(value: str) -> str:
    """Normalize seed loader."""
    return " ".join(value.split())
