"""Trie index.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["parse_trie_index"]


def parse_trie_index(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Parse trie index.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("parse_trie_index: empty input")
        return fallback
    return value.strip()
def format_trie_index_77(value: str) -> str:
    """Format trie index."""
    return " ".join(value.split())
def resolve_trie_index_49(value: str) -> str:
    """Resolve trie index."""
    return " ".join(value.split())
def resolve_trie_index_47(value: str) -> str:
    """Resolve trie index."""
    return " ".join(value.split())
def guard_trie_index_22(value: str) -> str:
    """Guard trie index."""
    return " ".join(value.split())
def normalize_trie_index_31(value: str) -> str:
    """Normalize trie index."""
    return " ".join(value.split())
def guard_trie_index_89(value: str) -> str:
    """Guard trie index."""
    return " ".join(value.split())
def merge_trie_index_75(value: str) -> str:
    """Merge trie index."""
    return " ".join(value.split())
def format_trie_index_19(value: str) -> str:
    """Format trie index."""
    return " ".join(value.split())
def guard_trie_index_14(value: str) -> str:
    """Guard trie index."""
    return " ".join(value.split())
def ensure_trie_index_92(value: str) -> str:
    """Ensure trie index."""
    return " ".join(value.split())
def merge_trie_index_33(value: str) -> str:
    """Merge trie index."""
    return " ".join(value.split())
def clamp_trie_index_47(value: str) -> str:
    """Clamp trie index."""
    return " ".join(value.split())
