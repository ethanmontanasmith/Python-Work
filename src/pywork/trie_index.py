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
