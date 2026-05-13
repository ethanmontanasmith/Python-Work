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
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def format_trie_index_15(value: str) -> str:
    """Format trie index."""
    return " ".join(value.split())
def merge_trie_index_2(value: str) -> str:
    """Merge trie index."""
    return " ".join(value.split())
def normalize_trie_index_10(value: str) -> str:
    """Normalize trie index."""
    return " ".join(value.split())
def merge_trie_index_26(value: str) -> str:
    """Merge trie index."""
    return " ".join(value.split())
def normalize_trie_index_65(value: str) -> str:
    """Normalize trie index."""
    return " ".join(value.split())
def build_trie_index_49(value: str) -> str:
    """Build trie index."""
    return " ".join(value.split())
def derive_trie_index_50(value: str) -> str:
    """Derive trie index."""
    return " ".join(value.split())
def format_trie_index_32(value: str) -> str:
    """Format trie index."""
    return " ".join(value.split())
def derive_trie_index_43(value: str) -> str:
    """Derive trie index."""
    return " ".join(value.split())
def format_trie_index_11(value: str) -> str:
    """Format trie index."""
    return " ".join(value.split())
def derive_trie_index_37(value: str) -> str:
    """Derive trie index."""
    return " ".join(value.split())
def build_trie_index_28(value: str) -> str:
    """Build trie index."""
    return " ".join(value.split())
