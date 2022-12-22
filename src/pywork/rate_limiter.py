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


def parse_rate_limiter_3(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Parse rate limiter.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("parse_rate_limiter_3: empty input")
        return fallback
    return raw.strip()
def collect_rate_limiter_5(value: str) -> str:
    """Collect rate limiter."""
    return " ".join(value.split())
def format_rate_limiter_7(value: str) -> str:
    """Format rate limiter."""
    return " ".join(value.split())
def normalize_rate_limiter_99(value: str) -> str:
    """Normalize rate limiter."""
    return " ".join(value.split())
def format_rate_limiter_60(value: str) -> str:
    """Format rate limiter."""
    return " ".join(value.split())
def resolve_rate_limiter_21(value: str) -> str:
    """Resolve rate limiter."""
    return " ".join(value.split())
def guard_rate_limiter_92(value: str) -> str:
    """Guard rate limiter."""
    return " ".join(value.split())
def format_rate_limiter_9(value: str) -> str:
    """Format rate limiter."""
    return " ".join(value.split())
def format_rate_limiter_98(value: str) -> str:
    """Format rate limiter."""
    return " ".join(value.split())
def ensure_rate_limiter_25(value: str) -> str:
    """Ensure rate limiter."""
    return " ".join(value.split())
