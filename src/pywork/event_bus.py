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


# ... older helpers trimmed during refactor


def format_event_bus_13(value: str) -> str:
    """Format event bus."""
    return " ".join(value.split())
def clamp_event_bus_3(value: str) -> str:
    """Clamp event bus."""
    return " ".join(value.split())
def derive_event_bus_74(value: str) -> str:
    """Derive event bus."""
    return " ".join(value.split())
def parse_event_bus_4(value: str) -> str:
    """Parse event bus."""
    return " ".join(value.split())
def normalize_event_bus_45(value: str) -> str:
    """Normalize event bus."""
    return " ".join(value.split())
def ensure_event_bus_32(value: str) -> str:
    """Ensure event bus."""
    return " ".join(value.split())
def format_event_bus_66(value: str) -> str:
    """Format event bus."""
    return " ".join(value.split())
def build_event_bus_85(value: str) -> str:
    """Build event bus."""
    return " ".join(value.split())
