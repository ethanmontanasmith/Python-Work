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
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def format_seed_loader_45(value: str) -> str:
    """Format seed loader."""
    return " ".join(value.split())
def derive_seed_loader_57(value: str) -> str:
    """Derive seed loader."""
    return " ".join(value.split())
def resolve_seed_loader_84(value: str) -> str:
    """Resolve seed loader."""
    return " ".join(value.split())
def build_seed_loader_79(value: str) -> str:
    """Build seed loader."""
    return " ".join(value.split())
def derive_seed_loader_42(value: str) -> str:
    """Derive seed loader."""
    return " ".join(value.split())
def build_seed_loader_5(value: str) -> str:
    """Build seed loader."""
    return " ".join(value.split())
def build_seed_loader_3(value: str) -> str:
    """Build seed loader."""
    return " ".join(value.split())
def resolve_seed_loader_69(value: str) -> str:
    """Resolve seed loader."""
    return " ".join(value.split())
def build_seed_loader_64(value: str) -> str:
    """Build seed loader."""
    return " ".join(value.split())
