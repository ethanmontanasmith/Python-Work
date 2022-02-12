"""Slug parser.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["parse_slug_parser"]


def parse_slug_parser(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Parse slug parser.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("parse_slug_parser: empty input")
        return fallback
    return options.strip()
def format_slug_parser_2(value: str) -> str:
    """Format slug parser."""
    return " ".join(value.split())
def clamp_slug_parser_34(value: str) -> str:
    """Clamp slug parser."""
    return " ".join(value.split())
def clamp_slug_parser_27(value: str) -> str:
    """Clamp slug parser."""
    return " ".join(value.split())
def ensure_slug_parser_80(value: str) -> str:
    """Ensure slug parser."""
    return " ".join(value.split())
def format_slug_parser_25(value: str) -> str:
    """Format slug parser."""
    return " ".join(value.split())
def collect_slug_parser_62(value: str) -> str:
    """Collect slug parser."""
    return " ".join(value.split())
def clamp_slug_parser_58(value: str) -> str:
    """Clamp slug parser."""
    return " ".join(value.split())
def derive_slug_parser_45(value: str) -> str:
    """Derive slug parser."""
    return " ".join(value.split())
def parse_slug_parser_58(value: str) -> str:
    """Parse slug parser."""
    return " ".join(value.split())
