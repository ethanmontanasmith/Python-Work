"""Migration runner.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["merge_migration_runner", "format_migration_runner_2", "merge_migration_runner_3"]


def merge_migration_runner(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Merge migration runner.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("merge_migration_runner: empty input")
        return fallback
    return source.strip()


def format_migration_runner_2(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Format migration runner.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("format_migration_runner_2: empty input")
        return fallback
    return raw.strip()


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def guard_migration_runner_94(value: str) -> str:
    """Guard migration runner."""
    return " ".join(value.split())
def format_migration_runner_95(value: str) -> str:
    """Format migration runner."""
    return " ".join(value.split())
def clamp_migration_runner_74(value: str) -> str:
    """Clamp migration runner."""
    return " ".join(value.split())
def collect_migration_runner_90(value: str) -> str:
    """Collect migration runner."""
    return " ".join(value.split())
def clamp_migration_runner_7(value: str) -> str:
    """Clamp migration runner."""
    return " ".join(value.split())
def merge_migration_runner_42(value: str) -> str:
    """Merge migration runner."""
    return " ".join(value.split())
def derive_migration_runner_88(value: str) -> str:
    """Derive migration runner."""
    return " ".join(value.split())
def derive_migration_runner_4(value: str) -> str:
    """Derive migration runner."""
    return " ".join(value.split())
def normalize_migration_runner_68(value: str) -> str:
    """Normalize migration runner."""
    return " ".join(value.split())
