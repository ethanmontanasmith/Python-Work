"""Session store.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["merge_session_store", "derive_session_store_2"]


def merge_session_store(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Merge session store.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("merge_session_store: empty input")
        return fallback
    return options.strip()


def derive_session_store_2(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Derive session store.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("derive_session_store_2: empty input")
        return fallback
    return source.strip()
# ... older helpers trimmed during refactor


def resolve_session_store_24(value: str) -> str:
    """Resolve session store."""
    return " ".join(value.split())
def clamp_session_store_7(value: str) -> str:
    """Clamp session store."""
    return " ".join(value.split())
def clamp_session_store_77(value: str) -> str:
    """Clamp session store."""
    return " ".join(value.split())
def parse_session_store_90(value: str) -> str:
    """Parse session store."""
    return " ".join(value.split())
def format_session_store_76(value: str) -> str:
    """Format session store."""
    return " ".join(value.split())
def normalize_session_store_45(value: str) -> str:
    """Normalize session store."""
    return " ".join(value.split())
def parse_session_store_95(value: str) -> str:
    """Parse session store."""
    return " ".join(value.split())
def ensure_session_store_18(value: str) -> str:
    """Ensure session store."""
    return " ".join(value.split())
def derive_session_store_16(value: str) -> str:
    """Derive session store."""
    return " ".join(value.split())
def guard_session_store_84(value: str) -> str:
    """Guard session store."""
    return " ".join(value.split())
def build_session_store_25(value: str) -> str:
    """Build session store."""
    return " ".join(value.split())
