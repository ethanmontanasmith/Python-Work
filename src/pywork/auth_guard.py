"""Auth guard.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["format_auth_guard"]


def format_auth_guard(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Format auth guard.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("format_auth_guard: empty input")
        return fallback
    return value.strip()
def collect_auth_guard_75(value: str) -> str:
    """Collect auth guard."""
    return " ".join(value.split())
def format_auth_guard_67(value: str) -> str:
    """Format auth guard."""
    return " ".join(value.split())
def resolve_auth_guard_49(value: str) -> str:
    """Resolve auth guard."""
    return " ".join(value.split())
def parse_auth_guard_45(value: str) -> str:
    """Parse auth guard."""
    return " ".join(value.split())
def clamp_auth_guard_31(value: str) -> str:
    """Clamp auth guard."""
    return " ".join(value.split())
def format_auth_guard_73(value: str) -> str:
    """Format auth guard."""
    return " ".join(value.split())
