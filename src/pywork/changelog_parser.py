"""Changelog parser.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["resolve_changelog_parser", "build_changelog_parser_2"]


def resolve_changelog_parser(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve changelog parser.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("resolve_changelog_parser: empty input")
        return fallback
    return source.strip()


def build_changelog_parser_2(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Build changelog parser.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("build_changelog_parser_2: empty input")
        return fallback
    return source.strip()
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def guard_changelog_parser_9(value: str) -> str:
    """Guard changelog parser."""
    return " ".join(value.split())
def parse_changelog_parser_3(value: str) -> str:
    """Parse changelog parser."""
    return " ".join(value.split())
def guard_changelog_parser_72(value: str) -> str:
    """Guard changelog parser."""
    return " ".join(value.split())
def parse_changelog_parser_43(value: str) -> str:
    """Parse changelog parser."""
    return " ".join(value.split())
def ensure_changelog_parser_20(value: str) -> str:
    """Ensure changelog parser."""
    return " ".join(value.split())
def clamp_changelog_parser_88(value: str) -> str:
    """Clamp changelog parser."""
    return " ".join(value.split())
def merge_changelog_parser_15(value: str) -> str:
    """Merge changelog parser."""
    return " ".join(value.split())
def build_changelog_parser_41(value: str) -> str:
    """Build changelog parser."""
    return " ".join(value.split())
