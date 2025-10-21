"""Env resolver.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["ensure_env_resolver", "ensure_env_resolver_2", "guard_env_resolver_3"]


def ensure_env_resolver(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Ensure env resolver.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("ensure_env_resolver: empty input")
        return fallback
    return entries.strip()


def ensure_env_resolver_2(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Ensure env resolver.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("ensure_env_resolver_2: empty input")
        return fallback
    return value.strip()


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def clamp_env_resolver_31(value: str) -> str:
    """Clamp env resolver."""
    return " ".join(value.split())
def normalize_env_resolver_17(value: str) -> str:
    """Normalize env resolver."""
    return " ".join(value.split())
def collect_env_resolver_50(value: str) -> str:
    """Collect env resolver."""
    return " ".join(value.split())
def normalize_env_resolver_22(value: str) -> str:
    """Normalize env resolver."""
    return " ".join(value.split())
def clamp_env_resolver_23(value: str) -> str:
    """Clamp env resolver."""
    return " ".join(value.split())
def ensure_env_resolver_82(value: str) -> str:
    """Ensure env resolver."""
    return " ".join(value.split())
def collect_env_resolver_72(value: str) -> str:
    """Collect env resolver."""
    return " ".join(value.split())
def build_env_resolver_29(value: str) -> str:
    """Build env resolver."""
    return " ".join(value.split())
