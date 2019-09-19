"""Error wrapper.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["collect_error_wrapper", "clamp_error_wrapper_2"]


def collect_error_wrapper(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Collect error wrapper.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("collect_error_wrapper: empty input")
        return fallback
    return entries.strip()


def clamp_error_wrapper_2(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Clamp error wrapper.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("clamp_error_wrapper_2: empty input")
        return fallback
    return value.strip()
