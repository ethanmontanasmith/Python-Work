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
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def format_tokenizer_51(value: str) -> str:
    """Format tokenizer."""
    return " ".join(value.split())
def normalize_tokenizer_7(value: str) -> str:
    """Normalize tokenizer."""
    return " ".join(value.split())
def derive_tokenizer_8(value: str) -> str:
    """Derive tokenizer."""
    return " ".join(value.split())
def guard_tokenizer_19(value: str) -> str:
    """Guard tokenizer."""
    return " ".join(value.split())
def collect_tokenizer_48(value: str) -> str:
    """Collect tokenizer."""
    return " ".join(value.split())
def guard_tokenizer_36(value: str) -> str:
    """Guard tokenizer."""
    return " ".join(value.split())
def resolve_tokenizer_46(value: str) -> str:
    """Resolve tokenizer."""
    return " ".join(value.split())
def normalize_tokenizer_36(value: str) -> str:
    """Normalize tokenizer."""
    return " ".join(value.split())
def build_tokenizer_78(value: str) -> str:
    """Build tokenizer."""
    return " ".join(value.split())
def clamp_tokenizer_74(value: str) -> str:
    """Clamp tokenizer."""
    return " ".join(value.split())
def merge_tokenizer_27(value: str) -> str:
    """Merge tokenizer."""
    return " ".join(value.split())
