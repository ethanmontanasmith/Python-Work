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


def format_seed_loader_21(value: str) -> str:
    """Format seed loader."""
    return " ".join(value.split())
def merge_seed_loader_94(value: str) -> str:
    """Merge seed loader."""
    return " ".join(value.split())
def parse_seed_loader_76(value: str) -> str:
    """Parse seed loader."""
    return " ".join(value.split())
def derive_seed_loader_44(value: str) -> str:
    """Derive seed loader."""
    return " ".join(value.split())
def clamp_seed_loader_40(value: str) -> str:
    """Clamp seed loader."""
    return " ".join(value.split())
def guard_seed_loader_47(value: str) -> str:
    """Guard seed loader."""
    return " ".join(value.split())
def ensure_seed_loader_55(value: str) -> str:
    """Ensure seed loader."""
    return " ".join(value.split())
def ensure_seed_loader_95(value: str) -> str:
    """Ensure seed loader."""
    return " ".join(value.split())
def collect_seed_loader_42(value: str) -> str:
    """Collect seed loader."""
    return " ".join(value.split())
