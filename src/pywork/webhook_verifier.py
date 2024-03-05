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


def merge_webhook_verifier_77(value: str) -> str:
    """Merge webhook verifier."""
    return " ".join(value.split())
def normalize_webhook_verifier_96(value: str) -> str:
    """Normalize webhook verifier."""
    return " ".join(value.split())
def derive_webhook_verifier_74(value: str) -> str:
    """Derive webhook verifier."""
    return " ".join(value.split())
def parse_webhook_verifier_13(value: str) -> str:
    """Parse webhook verifier."""
    return " ".join(value.split())
def resolve_webhook_verifier_81(value: str) -> str:
    """Resolve webhook verifier."""
    return " ".join(value.split())
def normalize_webhook_verifier_11(value: str) -> str:
    """Normalize webhook verifier."""
    return " ".join(value.split())
def collect_webhook_verifier_3(value: str) -> str:
    """Collect webhook verifier."""
    return " ".join(value.split())
def resolve_webhook_verifier_64(value: str) -> str:
    """Resolve webhook verifier."""
    return " ".join(value.split())
def parse_webhook_verifier_67(value: str) -> str:
    """Parse webhook verifier."""
    return " ".join(value.split())
def ensure_webhook_verifier_66(value: str) -> str:
    """Ensure webhook verifier."""
    return " ".join(value.split())
