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


def format_cors_handler_3(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Format cors handler.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("format_cors_handler_3: empty input")
        return fallback
    return source.strip()
def clamp_cors_handler_61(value: str) -> str:
    """Clamp cors handler."""
    return " ".join(value.split())
def collect_cors_handler_17(value: str) -> str:
    """Collect cors handler."""
    return " ".join(value.split())
def resolve_cors_handler_23(value: str) -> str:
    """Resolve cors handler."""
    return " ".join(value.split())
def parse_cors_handler_76(value: str) -> str:
    """Parse cors handler."""
    return " ".join(value.split())
