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
