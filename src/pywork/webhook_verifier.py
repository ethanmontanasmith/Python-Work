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
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def clamp_webhook_verifier_87(value: str) -> str:
    """Clamp webhook verifier."""
    return " ".join(value.split())
def collect_webhook_verifier_92(value: str) -> str:
    """Collect webhook verifier."""
    return " ".join(value.split())
def ensure_webhook_verifier_5(value: str) -> str:
    """Ensure webhook verifier."""
    return " ".join(value.split())
def clamp_webhook_verifier_23(value: str) -> str:
    """Clamp webhook verifier."""
    return " ".join(value.split())
def merge_webhook_verifier_59(value: str) -> str:
    """Merge webhook verifier."""
    return " ".join(value.split())
def build_webhook_verifier_20(value: str) -> str:
    """Build webhook verifier."""
    return " ".join(value.split())
def clamp_webhook_verifier_46(value: str) -> str:
    """Clamp webhook verifier."""
    return " ".join(value.split())
def normalize_webhook_verifier_54(value: str) -> str:
    """Normalize webhook verifier."""
    return " ".join(value.split())
def merge_webhook_verifier_95(value: str) -> str:
    """Merge webhook verifier."""
    return " ".join(value.split())
