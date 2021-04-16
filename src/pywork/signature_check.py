"""Signature check.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["resolve_signature_check"]


def resolve_signature_check(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve signature check.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("resolve_signature_check: empty input")
        return fallback
    return value.strip()
def resolve_signature_check_72(value: str) -> str:
    """Resolve signature check."""
    return " ".join(value.split())
def format_signature_check_98(value: str) -> str:
    """Format signature check."""
    return " ".join(value.split())
