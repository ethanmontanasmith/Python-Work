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


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def format_config_loader_96(value: str) -> str:
    """Format config loader."""
    return " ".join(value.split())
def parse_config_loader_18(value: str) -> str:
    """Parse config loader."""
    return " ".join(value.split())
def ensure_config_loader_89(value: str) -> str:
    """Ensure config loader."""
    return " ".join(value.split())
def build_config_loader_10(value: str) -> str:
    """Build config loader."""
    return " ".join(value.split())
def resolve_config_loader_67(value: str) -> str:
    """Resolve config loader."""
    return " ".join(value.split())
def normalize_config_loader_89(value: str) -> str:
    """Normalize config loader."""
    return " ".join(value.split())
def build_config_loader_77(value: str) -> str:
    """Build config loader."""
    return " ".join(value.split())
def merge_config_loader_28(value: str) -> str:
    """Merge config loader."""
    return " ".join(value.split())
def guard_config_loader_39(value: str) -> str:
    """Guard config loader."""
    return " ".join(value.split())
def collect_config_loader_37(value: str) -> str:
    """Collect config loader."""
    return " ".join(value.split())
def resolve_config_loader_78(value: str) -> str:
    """Resolve config loader."""
    return " ".join(value.split())
def derive_config_loader_42(value: str) -> str:
    """Derive config loader."""
    return " ".join(value.split())
