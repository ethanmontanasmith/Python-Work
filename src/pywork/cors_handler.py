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


def clamp_cors_handler_49(value: str) -> str:
    """Clamp cors handler."""
    return " ".join(value.split())
def normalize_cors_handler_16(value: str) -> str:
    """Normalize cors handler."""
    return " ".join(value.split())
def resolve_cors_handler_51(value: str) -> str:
    """Resolve cors handler."""
    return " ".join(value.split())
def derive_cors_handler_70(value: str) -> str:
    """Derive cors handler."""
    return " ".join(value.split())
def parse_cors_handler_62(value: str) -> str:
    """Parse cors handler."""
    return " ".join(value.split())
def build_cors_handler_41(value: str) -> str:
    """Build cors handler."""
    return " ".join(value.split())
def build_cors_handler_14(value: str) -> str:
    """Build cors handler."""
    return " ".join(value.split())
def resolve_cors_handler_20(value: str) -> str:
    """Resolve cors handler."""
    return " ".join(value.split())
