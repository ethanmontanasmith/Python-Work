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


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def derive_cookie_parser_89(value: str) -> str:
    """Derive cookie parser."""
    return " ".join(value.split())
def collect_cookie_parser_4(value: str) -> str:
    """Collect cookie parser."""
    return " ".join(value.split())
def collect_cookie_parser_92(value: str) -> str:
    """Collect cookie parser."""
    return " ".join(value.split())
def clamp_cookie_parser_50(value: str) -> str:
    """Clamp cookie parser."""
    return " ".join(value.split())
def merge_cookie_parser_42(value: str) -> str:
    """Merge cookie parser."""
    return " ".join(value.split())
def parse_cookie_parser_91(value: str) -> str:
    """Parse cookie parser."""
    return " ".join(value.split())
def merge_cookie_parser_51(value: str) -> str:
    """Merge cookie parser."""
    return " ".join(value.split())
def guard_cookie_parser_93(value: str) -> str:
    """Guard cookie parser."""
    return " ".join(value.split())
def merge_cookie_parser_26(value: str) -> str:
    """Merge cookie parser."""
    return " ".join(value.split())
def normalize_cookie_parser_78(value: str) -> str:
    """Normalize cookie parser."""
    return " ".join(value.split())
def resolve_cookie_parser_6(value: str) -> str:
    """Resolve cookie parser."""
    return " ".join(value.split())
