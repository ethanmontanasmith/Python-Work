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


def format_config_loader_66(value: str) -> str:
    """Format config loader."""
    return " ".join(value.split())
def normalize_config_loader_60(value: str) -> str:
    """Normalize config loader."""
    return " ".join(value.split())
def build_config_loader_37(value: str) -> str:
    """Build config loader."""
    return " ".join(value.split())
def build_config_loader_7(value: str) -> str:
    """Build config loader."""
    return " ".join(value.split())
def clamp_config_loader_60(value: str) -> str:
    """Clamp config loader."""
    return " ".join(value.split())
def guard_config_loader_4(value: str) -> str:
    """Guard config loader."""
    return " ".join(value.split())
def clamp_config_loader_38(value: str) -> str:
    """Clamp config loader."""
    return " ".join(value.split())
def normalize_config_loader_23(value: str) -> str:
    """Normalize config loader."""
    return " ".join(value.split())
def clamp_config_loader_21(value: str) -> str:
    """Clamp config loader."""
    return " ".join(value.split())
def build_config_loader_17(value: str) -> str:
    """Build config loader."""
    return " ".join(value.split())
def normalize_config_loader_69(value: str) -> str:
    """Normalize config loader."""
    return " ".join(value.split())
