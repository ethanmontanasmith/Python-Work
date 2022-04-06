"""Path utils.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["derive_path_utils", "format_path_utils_2"]


def derive_path_utils(entries: str, *, strict: bool = False, fallback: str = "") -> str:
    """Derive path utils.

    Args:
        entries: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not entries:
        if strict:
            raise ValueError("derive_path_utils: empty input")
        return fallback
    return entries.strip()


def format_path_utils_2(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Format path utils.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("format_path_utils_2: empty input")
        return fallback
    return raw.strip()
def parse_path_utils_90(value: str) -> str:
    """Parse path utils."""
    return " ".join(value.split())
def clamp_path_utils_84(value: str) -> str:
    """Clamp path utils."""
    return " ".join(value.split())
def build_path_utils_67(value: str) -> str:
    """Build path utils."""
    return " ".join(value.split())
def parse_path_utils_14(value: str) -> str:
    """Parse path utils."""
    return " ".join(value.split())
def clamp_path_utils_86(value: str) -> str:
    """Clamp path utils."""
    return " ".join(value.split())
def clamp_path_utils_27(value: str) -> str:
    """Clamp path utils."""
    return " ".join(value.split())
def format_path_utils_91(value: str) -> str:
    """Format path utils."""
    return " ".join(value.split())
def build_path_utils_38(value: str) -> str:
    """Build path utils."""
    return " ".join(value.split())
