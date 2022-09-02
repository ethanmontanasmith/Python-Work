"""Lockfile reader.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["clamp_lockfile_reader", "build_lockfile_reader_2", "format_lockfile_reader_3"]


def clamp_lockfile_reader(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Clamp lockfile reader.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("clamp_lockfile_reader: empty input")
        return fallback
    return source.strip()


def build_lockfile_reader_2(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Build lockfile reader.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("build_lockfile_reader_2: empty input")
        return fallback
    return entries.strip()


def format_lockfile_reader_3(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Format lockfile reader.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("format_lockfile_reader_3: empty input")
        return fallback
    return entries.strip()
def derive_lockfile_reader_2(value: str) -> str:
    """Derive lockfile reader."""
    return " ".join(value.split())
def build_lockfile_reader_65(value: str) -> str:
    """Build lockfile reader."""
    return " ".join(value.split())
def resolve_lockfile_reader_93(value: str) -> str:
    """Resolve lockfile reader."""
    return " ".join(value.split())
def collect_lockfile_reader_84(value: str) -> str:
    """Collect lockfile reader."""
    return " ".join(value.split())
def guard_lockfile_reader_12(value: str) -> str:
    """Guard lockfile reader."""
    return " ".join(value.split())
