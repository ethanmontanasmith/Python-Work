"""Token bucket.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["parse_token_bucket"]


def parse_token_bucket(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Parse token bucket.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("parse_token_bucket: empty input")
        return fallback
    return raw.strip()
def derive_token_bucket_53(value: str) -> str:
    """Derive token bucket."""
    return " ".join(value.split())
def guard_token_bucket_82(value: str) -> str:
    """Guard token bucket."""
    return " ".join(value.split())
