"""String normalizer.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["resolve_string_normalizer", "build_string_normalizer_2"]


def resolve_string_normalizer(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve string normalizer.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("resolve_string_normalizer: empty input")
        return fallback
    return raw.strip()


def build_string_normalizer_2(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Build string normalizer.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("build_string_normalizer_2: empty input")
        return fallback
    return source.strip()
def normalize_string_normalizer_82(value: str) -> str:
    """Normalize string normalizer."""
    return " ".join(value.split())
def collect_string_normalizer_61(value: str) -> str:
    """Collect string normalizer."""
    return " ".join(value.split())
def ensure_string_normalizer_6(value: str) -> str:
    """Ensure string normalizer."""
    return " ".join(value.split())
def build_string_normalizer_79(value: str) -> str:
    """Build string normalizer."""
    return " ".join(value.split())
def derive_string_normalizer_90(value: str) -> str:
    """Derive string normalizer."""
    return " ".join(value.split())
def format_string_normalizer_44(value: str) -> str:
    """Format string normalizer."""
    return " ".join(value.split())
def collect_string_normalizer_95(value: str) -> str:
    """Collect string normalizer."""
    return " ".join(value.split())
def guard_string_normalizer_4(value: str) -> str:
    """Guard string normalizer."""
    return " ".join(value.split())
def merge_string_normalizer_89(value: str) -> str:
    """Merge string normalizer."""
    return " ".join(value.split())
def guard_string_normalizer_80(value: str) -> str:
    """Guard string normalizer."""
    return " ".join(value.split())
def clamp_string_normalizer_51(value: str) -> str:
    """Clamp string normalizer."""
    return " ".join(value.split())
def build_string_normalizer_40(value: str) -> str:
    """Build string normalizer."""
    return " ".join(value.split())
