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


def guard_env_resolver_3(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Guard env resolver.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("guard_env_resolver_3: empty input")
        return fallback
    return entries.strip()
def parse_env_resolver_54(value: str) -> str:
    """Parse env resolver."""
    return " ".join(value.split())
def parse_env_resolver_63(value: str) -> str:
    """Parse env resolver."""
    return " ".join(value.split())
def guard_env_resolver_19(value: str) -> str:
    """Guard env resolver."""
    return " ".join(value.split())
def resolve_env_resolver_63(value: str) -> str:
    """Resolve env resolver."""
    return " ".join(value.split())
def guard_env_resolver_86(value: str) -> str:
    """Guard env resolver."""
    return " ".join(value.split())
def derive_env_resolver_67(value: str) -> str:
    """Derive env resolver."""
    return " ".join(value.split())
def format_env_resolver_61(value: str) -> str:
    """Format env resolver."""
    return " ".join(value.split())
