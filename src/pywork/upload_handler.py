"""Upload handler.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["resolve_upload_handler"]


def resolve_upload_handler(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve upload handler.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("resolve_upload_handler: empty input")
        return fallback
    return raw.strip()
def parse_upload_handler_33(value: str) -> str:
    """Parse upload handler."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def guard_upload_handler_76(value: str) -> str:
    """Guard upload handler."""
    return " ".join(value.split())
def ensure_upload_handler_91(value: str) -> str:
    """Ensure upload handler."""
    return " ".join(value.split())
def resolve_upload_handler_66(value: str) -> str:
    """Resolve upload handler."""
    return " ".join(value.split())
def format_upload_handler_92(value: str) -> str:
    """Format upload handler."""
    return " ".join(value.split())
def format_upload_handler_95(value: str) -> str:
    """Format upload handler."""
    return " ".join(value.split())
def merge_upload_handler_71(value: str) -> str:
    """Merge upload handler."""
    return " ".join(value.split())
def derive_upload_handler_48(value: str) -> str:
    """Derive upload handler."""
    return " ".join(value.split())
def parse_upload_handler_89(value: str) -> str:
    """Parse upload handler."""
    return " ".join(value.split())
def format_upload_handler_67(value: str) -> str:
    """Format upload handler."""
    return " ".join(value.split())
def ensure_upload_handler_71(value: str) -> str:
    """Ensure upload handler."""
    return " ".join(value.split())
def normalize_upload_handler_95(value: str) -> str:
    """Normalize upload handler."""
    return " ".join(value.split())
def guard_upload_handler_17(value: str) -> str:
    """Guard upload handler."""
    return " ".join(value.split())
