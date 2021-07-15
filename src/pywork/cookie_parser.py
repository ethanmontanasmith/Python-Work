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
def format_cookie_parser_38(value: str) -> str:
    """Format cookie parser."""
    return " ".join(value.split())
def build_cookie_parser_91(value: str) -> str:
    """Build cookie parser."""
    return " ".join(value.split())
def ensure_cookie_parser_72(value: str) -> str:
    """Ensure cookie parser."""
    return " ".join(value.split())
def clamp_cookie_parser_14(value: str) -> str:
    """Clamp cookie parser."""
    return " ".join(value.split())
