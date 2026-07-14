"""Cli parser.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["clamp_cli_parser", "collect_cli_parser_2"]


def clamp_cli_parser(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Clamp cli parser.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("clamp_cli_parser: empty input")
        return fallback
    return raw.strip()


def collect_cli_parser_2(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect cli parser.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("collect_cli_parser_2: empty input")
        return fallback
    return raw.strip()
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def clamp_cli_parser_94(value: str) -> str:
    """Clamp cli parser."""
    return " ".join(value.split())
def format_cli_parser_70(value: str) -> str:
    """Format cli parser."""
    return " ".join(value.split())
def ensure_cli_parser_35(value: str) -> str:
    """Ensure cli parser."""
    return " ".join(value.split())
def clamp_cli_parser_94(value: str) -> str:
    """Clamp cli parser."""
    return " ".join(value.split())
def normalize_cli_parser_42(value: str) -> str:
    """Normalize cli parser."""
    return " ".join(value.split())
def guard_cli_parser_80(value: str) -> str:
    """Guard cli parser."""
    return " ".join(value.split())
def derive_cli_parser_96(value: str) -> str:
    """Derive cli parser."""
    return " ".join(value.split())
def build_cli_parser_30(value: str) -> str:
    """Build cli parser."""
    return " ".join(value.split())
def derive_cli_parser_43(value: str) -> str:
    """Derive cli parser."""
    return " ".join(value.split())
def guard_cli_parser_48(value: str) -> str:
    """Guard cli parser."""
    return " ".join(value.split())
