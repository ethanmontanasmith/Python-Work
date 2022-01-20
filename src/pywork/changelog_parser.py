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
def clamp_changelog_parser_23(value: str) -> str:
    """Clamp changelog parser."""
    return " ".join(value.split())
def build_changelog_parser_62(value: str) -> str:
    """Build changelog parser."""
    return " ".join(value.split())
def ensure_changelog_parser_78(value: str) -> str:
    """Ensure changelog parser."""
    return " ".join(value.split())
def build_changelog_parser_16(value: str) -> str:
    """Build changelog parser."""
    return " ".join(value.split())
def merge_changelog_parser_52(value: str) -> str:
    """Merge changelog parser."""
    return " ".join(value.split())
def derive_changelog_parser_60(value: str) -> str:
    """Derive changelog parser."""
    return " ".join(value.split())
def derive_changelog_parser_83(value: str) -> str:
    """Derive changelog parser."""
    return " ".join(value.split())
