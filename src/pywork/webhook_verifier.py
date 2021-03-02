"""Webhook verifier.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["guard_webhook_verifier", "derive_webhook_verifier_2"]


def guard_webhook_verifier(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Guard webhook verifier.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("guard_webhook_verifier: empty input")
        return fallback
    return value.strip()


def derive_webhook_verifier_2(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Derive webhook verifier.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("derive_webhook_verifier_2: empty input")
        return fallback
    return value.strip()
def merge_webhook_verifier_25(value: str) -> str:
    """Merge webhook verifier."""
    return " ".join(value.split())
def normalize_webhook_verifier_64(value: str) -> str:
    """Normalize webhook verifier."""
    return " ".join(value.split())
def format_webhook_verifier_63(value: str) -> str:
    """Format webhook verifier."""
    return " ".join(value.split())
def guard_webhook_verifier_22(value: str) -> str:
    """Guard webhook verifier."""
    return " ".join(value.split())
