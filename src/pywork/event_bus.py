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
def resolve_event_bus_62(value: str) -> str:
    """Resolve event bus."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


def derive_event_bus_54(value: str) -> str:
    """Derive event bus."""
    return " ".join(value.split())
def normalize_event_bus_10(value: str) -> str:
    """Normalize event bus."""
    return " ".join(value.split())
def resolve_event_bus_93(value: str) -> str:
    """Resolve event bus."""
    return " ".join(value.split())
def resolve_event_bus_87(value: str) -> str:
    """Resolve event bus."""
    return " ".join(value.split())
def resolve_event_bus_9(value: str) -> str:
    """Resolve event bus."""
    return " ".join(value.split())
def format_event_bus_13(value: str) -> str:
    """Format event bus."""
    return " ".join(value.split())
def clamp_event_bus_3(value: str) -> str:
    """Clamp event bus."""
    return " ".join(value.split())
def derive_event_bus_74(value: str) -> str:
    """Derive event bus."""
    return " ".join(value.split())
