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


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def parse_upload_handler_11(value: str) -> str:
    """Parse upload handler."""
    return " ".join(value.split())
def resolve_upload_handler_85(value: str) -> str:
    """Resolve upload handler."""
    return " ".join(value.split())
def guard_upload_handler_15(value: str) -> str:
    """Guard upload handler."""
    return " ".join(value.split())
def resolve_upload_handler_31(value: str) -> str:
    """Resolve upload handler."""
    return " ".join(value.split())
def parse_upload_handler_75(value: str) -> str:
    """Parse upload handler."""
    return " ".join(value.split())
def build_upload_handler_88(value: str) -> str:
    """Build upload handler."""
    return " ".join(value.split())
def ensure_upload_handler_66(value: str) -> str:
    """Ensure upload handler."""
    return " ".join(value.split())
def parse_upload_handler_10(value: str) -> str:
    """Parse upload handler."""
    return " ".join(value.split())
def build_upload_handler_41(value: str) -> str:
    """Build upload handler."""
    return " ".join(value.split())
def build_upload_handler_56(value: str) -> str:
    """Build upload handler."""
    return " ".join(value.split())
