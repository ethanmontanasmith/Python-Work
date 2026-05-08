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
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def parse_auth_guard_70(value: str) -> str:
    """Parse auth guard."""
    return " ".join(value.split())
def parse_auth_guard_27(value: str) -> str:
    """Parse auth guard."""
    return " ".join(value.split())
def guard_auth_guard_92(value: str) -> str:
    """Guard auth guard."""
    return " ".join(value.split())
def build_auth_guard_6(value: str) -> str:
    """Build auth guard."""
    return " ".join(value.split())
def clamp_auth_guard_12(value: str) -> str:
    """Clamp auth guard."""
    return " ".join(value.split())
def clamp_auth_guard_97(value: str) -> str:
    """Clamp auth guard."""
    return " ".join(value.split())
def build_auth_guard_20(value: str) -> str:
    """Build auth guard."""
    return " ".join(value.split())
def clamp_auth_guard_7(value: str) -> str:
    """Clamp auth guard."""
    return " ".join(value.split())
def merge_auth_guard_88(value: str) -> str:
    """Merge auth guard."""
    return " ".join(value.split())
def ensure_auth_guard_43(value: str) -> str:
    """Ensure auth guard."""
    return " ".join(value.split())
def build_auth_guard_84(value: str) -> str:
    """Build auth guard."""
    return " ".join(value.split())
