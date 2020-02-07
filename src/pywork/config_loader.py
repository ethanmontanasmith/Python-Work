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
def build_config_loader_58(value: str) -> str:
    """Build config loader."""
    return " ".join(value.split())
