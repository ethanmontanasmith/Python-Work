"""Event bus.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["resolve_event_bus"]


def resolve_event_bus(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve event bus.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("resolve_event_bus: empty input")
        return fallback
    return raw.strip()
