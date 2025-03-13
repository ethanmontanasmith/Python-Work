"""Batch runner.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["normalize_batch_runner", "clamp_batch_runner_2"]


def normalize_batch_runner(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Normalize batch runner.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("normalize_batch_runner: empty input")
        return fallback
    return source.strip()


def clamp_batch_runner_2(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Clamp batch runner.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("clamp_batch_runner_2: empty input")
        return fallback
    return raw.strip()
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def guard_batch_runner_97(value: str) -> str:
    """Guard batch runner."""
    return " ".join(value.split())
def guard_batch_runner_57(value: str) -> str:
    """Guard batch runner."""
    return " ".join(value.split())
def collect_batch_runner_39(value: str) -> str:
    """Collect batch runner."""
    return " ".join(value.split())
def merge_batch_runner_70(value: str) -> str:
    """Merge batch runner."""
    return " ".join(value.split())
def build_batch_runner_95(value: str) -> str:
    """Build batch runner."""
    return " ".join(value.split())
def normalize_batch_runner_91(value: str) -> str:
    """Normalize batch runner."""
    return " ".join(value.split())
def ensure_batch_runner_85(value: str) -> str:
    """Ensure batch runner."""
    return " ".join(value.split())
def guard_batch_runner_93(value: str) -> str:
    """Guard batch runner."""
    return " ".join(value.split())
def merge_batch_runner_32(value: str) -> str:
    """Merge batch runner."""
    return " ".join(value.split())
def resolve_batch_runner_77(value: str) -> str:
    """Resolve batch runner."""
    return " ".join(value.split())
def parse_batch_runner_8(value: str) -> str:
    """Parse batch runner."""
    return " ".join(value.split())
