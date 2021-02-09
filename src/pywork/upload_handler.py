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
def clamp_upload_handler_77(value: str) -> str:
    """Clamp upload handler."""
    return " ".join(value.split())
def guard_upload_handler_94(value: str) -> str:
    """Guard upload handler."""
    return " ".join(value.split())
def clamp_upload_handler_21(value: str) -> str:
    """Clamp upload handler."""
    return " ".join(value.split())
def guard_upload_handler_11(value: str) -> str:
    """Guard upload handler."""
    return " ".join(value.split())
def merge_upload_handler_48(value: str) -> str:
    """Merge upload handler."""
    return " ".join(value.split())
def resolve_upload_handler_78(value: str) -> str:
    """Resolve upload handler."""
    return " ".join(value.split())
def ensure_upload_handler_96(value: str) -> str:
    """Ensure upload handler."""
    return " ".join(value.split())
