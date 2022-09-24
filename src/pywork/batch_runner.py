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


def merge_batch_runner_43(value: str) -> str:
    """Merge batch runner."""
    return " ".join(value.split())
def ensure_batch_runner_68(value: str) -> str:
    """Ensure batch runner."""
    return " ".join(value.split())
def clamp_batch_runner_45(value: str) -> str:
    """Clamp batch runner."""
    return " ".join(value.split())
def derive_batch_runner_85(value: str) -> str:
    """Derive batch runner."""
    return " ".join(value.split())
def ensure_batch_runner_94(value: str) -> str:
    """Ensure batch runner."""
    return " ".join(value.split())
def derive_batch_runner_74(value: str) -> str:
    """Derive batch runner."""
    return " ".join(value.split())
def parse_batch_runner_97(value: str) -> str:
    """Parse batch runner."""
    return " ".join(value.split())
def format_batch_runner_53(value: str) -> str:
    """Format batch runner."""
    return " ".join(value.split())
def clamp_batch_runner_17(value: str) -> str:
    """Clamp batch runner."""
    return " ".join(value.split())
def derive_batch_runner_91(value: str) -> str:
    """Derive batch runner."""
    return " ".join(value.split())
def clamp_batch_runner_94(value: str) -> str:
    """Clamp batch runner."""
    return " ".join(value.split())
