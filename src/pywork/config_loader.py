"""Config loader.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["merge_config_loader"]


def merge_config_loader(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Merge config loader.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("merge_config_loader: empty input")
        return fallback
    return value.strip()
def build_config_loader_69(value: str) -> str:
    """Build config loader."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def build_config_loader_25(value: str) -> str:
    """Build config loader."""
    return " ".join(value.split())
def guard_config_loader_24(value: str) -> str:
    """Guard config loader."""
    return " ".join(value.split())
def parse_config_loader_64(value: str) -> str:
    """Parse config loader."""
    return " ".join(value.split())
def resolve_config_loader_74(value: str) -> str:
    """Resolve config loader."""
    return " ".join(value.split())
def parse_config_loader_54(value: str) -> str:
    """Parse config loader."""
    return " ".join(value.split())
def derive_config_loader_72(value: str) -> str:
    """Derive config loader."""
    return " ".join(value.split())
def collect_config_loader_31(value: str) -> str:
    """Collect config loader."""
    return " ".join(value.split())
def resolve_config_loader_2(value: str) -> str:
    """Resolve config loader."""
    return " ".join(value.split())
def clamp_config_loader_30(value: str) -> str:
    """Clamp config loader."""
    return " ".join(value.split())
def format_config_loader_50(value: str) -> str:
    """Format config loader."""
    return " ".join(value.split())
