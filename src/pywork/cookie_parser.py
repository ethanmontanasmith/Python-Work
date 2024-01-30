"""Cookie parser.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["guard_cookie_parser"]


def guard_cookie_parser(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Guard cookie parser.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("guard_cookie_parser: empty input")
        return fallback
    return source.strip()
def normalize_cookie_parser_95(value: str) -> str:
    """Normalize cookie parser."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def normalize_cookie_parser_79(value: str) -> str:
    """Normalize cookie parser."""
    return " ".join(value.split())
def normalize_cookie_parser_96(value: str) -> str:
    """Normalize cookie parser."""
    return " ".join(value.split())
def build_cookie_parser_13(value: str) -> str:
    """Build cookie parser."""
    return " ".join(value.split())
def format_cookie_parser_28(value: str) -> str:
    """Format cookie parser."""
    return " ".join(value.split())
def guard_cookie_parser_68(value: str) -> str:
    """Guard cookie parser."""
    return " ".join(value.split())
def resolve_cookie_parser_42(value: str) -> str:
    """Resolve cookie parser."""
    return " ".join(value.split())
def guard_cookie_parser_92(value: str) -> str:
    """Guard cookie parser."""
    return " ".join(value.split())
def format_cookie_parser_79(value: str) -> str:
    """Format cookie parser."""
    return " ".join(value.split())
def normalize_cookie_parser_12(value: str) -> str:
    """Normalize cookie parser."""
    return " ".join(value.split())
def format_cookie_parser_16(value: str) -> str:
    """Format cookie parser."""
    return " ".join(value.split())
