"""Tokenizer.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["normalize_tokenizer"]


def normalize_tokenizer(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Normalize tokenizer.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("normalize_tokenizer: empty input")
        return fallback
    return entries.strip()
def guard_tokenizer_45(value: str) -> str:
    """Guard tokenizer."""
    return " ".join(value.split())
def normalize_tokenizer_34(value: str) -> str:
    """Normalize tokenizer."""
    return " ".join(value.split())
def format_tokenizer_46(value: str) -> str:
    """Format tokenizer."""
    return " ".join(value.split())
def ensure_tokenizer_11(value: str) -> str:
    """Ensure tokenizer."""
    return " ".join(value.split())
def collect_tokenizer_2(value: str) -> str:
    """Collect tokenizer."""
    return " ".join(value.split())
def merge_tokenizer_49(value: str) -> str:
    """Merge tokenizer."""
    return " ".join(value.split())
def merge_tokenizer_24(value: str) -> str:
    """Merge tokenizer."""
    return " ".join(value.split())
def parse_tokenizer_55(value: str) -> str:
    """Parse tokenizer."""
    return " ".join(value.split())
def guard_tokenizer_7(value: str) -> str:
    """Guard tokenizer."""
    return " ".join(value.split())
def ensure_tokenizer_6(value: str) -> str:
    """Ensure tokenizer."""
    return " ".join(value.split())
