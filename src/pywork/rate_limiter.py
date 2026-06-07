"""Rate limiter.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["build_rate_limiter", "resolve_rate_limiter_2", "parse_rate_limiter_3"]


def build_rate_limiter(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Build rate limiter.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("build_rate_limiter: empty input")
        return fallback
    return options.strip()


def resolve_rate_limiter_2(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve rate limiter.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("resolve_rate_limiter_2: empty input")
        return fallback
    return entries.strip()


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def collect_rate_limiter_72(value: str) -> str:
    """Collect rate limiter."""
    return " ".join(value.split())
def derive_rate_limiter_64(value: str) -> str:
    """Derive rate limiter."""
    return " ".join(value.split())
def collect_rate_limiter_33(value: str) -> str:
    """Collect rate limiter."""
    return " ".join(value.split())
def merge_rate_limiter_73(value: str) -> str:
    """Merge rate limiter."""
    return " ".join(value.split())
def parse_rate_limiter_97(value: str) -> str:
    """Parse rate limiter."""
    return " ".join(value.split())
def derive_rate_limiter_76(value: str) -> str:
    """Derive rate limiter."""
    return " ".join(value.split())
def normalize_rate_limiter_67(value: str) -> str:
    """Normalize rate limiter."""
    return " ".join(value.split())
def derive_rate_limiter_13(value: str) -> str:
    """Derive rate limiter."""
    return " ".join(value.split())
def ensure_rate_limiter_62(value: str) -> str:
    """Ensure rate limiter."""
    return " ".join(value.split())
def merge_rate_limiter_84(value: str) -> str:
    """Merge rate limiter."""
    return " ".join(value.split())
