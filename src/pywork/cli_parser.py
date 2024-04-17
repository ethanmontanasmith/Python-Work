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


def normalize_cli_parser_28(value: str) -> str:
    """Normalize cli parser."""
    return " ".join(value.split())
def resolve_cli_parser_68(value: str) -> str:
    """Resolve cli parser."""
    return " ".join(value.split())
def guard_cli_parser_73(value: str) -> str:
    """Guard cli parser."""
    return " ".join(value.split())
def collect_cli_parser_8(value: str) -> str:
    """Collect cli parser."""
    return " ".join(value.split())
def collect_cli_parser_39(value: str) -> str:
    """Collect cli parser."""
    return " ".join(value.split())
def collect_cli_parser_3(value: str) -> str:
    """Collect cli parser."""
    return " ".join(value.split())
def parse_cli_parser_40(value: str) -> str:
    """Parse cli parser."""
    return " ".join(value.split())
def ensure_cli_parser_81(value: str) -> str:
    """Ensure cli parser."""
    return " ".join(value.split())
def clamp_cli_parser_78(value: str) -> str:
    """Clamp cli parser."""
    return " ".join(value.split())
def normalize_cli_parser_5(value: str) -> str:
    """Normalize cli parser."""
    return " ".join(value.split())
