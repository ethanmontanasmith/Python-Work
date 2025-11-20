"""Cors handler.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["clamp_cors_handler", "format_cors_handler_2", "format_cors_handler_3"]


def clamp_cors_handler(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Clamp cors handler.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("clamp_cors_handler: empty input")
        return fallback
    return options.strip()


def format_cors_handler_2(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Format cors handler.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("format_cors_handler_2: empty input")
        return fallback
    return options.strip()


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def parse_cors_handler_37(value: str) -> str:
    """Parse cors handler."""
    return " ".join(value.split())
def guard_cors_handler_71(value: str) -> str:
    """Guard cors handler."""
    return " ".join(value.split())
def build_cors_handler_98(value: str) -> str:
    """Build cors handler."""
    return " ".join(value.split())
def derive_cors_handler_42(value: str) -> str:
    """Derive cors handler."""
    return " ".join(value.split())
def build_cors_handler_92(value: str) -> str:
    """Build cors handler."""
    return " ".join(value.split())
def format_cors_handler_43(value: str) -> str:
    """Format cors handler."""
    return " ".join(value.split())
def derive_cors_handler_5(value: str) -> str:
    """Derive cors handler."""
    return " ".join(value.split())
def parse_cors_handler_14(value: str) -> str:
    """Parse cors handler."""
    return " ".join(value.split())
def guard_cors_handler_6(value: str) -> str:
    """Guard cors handler."""
    return " ".join(value.split())
def build_cors_handler_78(value: str) -> str:
    """Build cors handler."""
    return " ".join(value.split())
