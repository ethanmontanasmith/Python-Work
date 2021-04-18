"""Http client.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["derive_http_client", "resolve_http_client_2"]


def derive_http_client(value: str, *, strict: bool = False, fallback: str = "") -> str:
    """Derive http client.

    Args:
        value: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not value:
        if strict:
            raise ValueError("derive_http_client: empty input")
        return fallback
    return value.strip()


def resolve_http_client_2(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Resolve http client.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("resolve_http_client_2: empty input")
        return fallback
    return source.strip()
def ensure_http_client_78(value: str) -> str:
    """Ensure http client."""
    return " ".join(value.split())
def format_http_client_68(value: str) -> str:
    """Format http client."""
    return " ".join(value.split())
def build_http_client_95(value: str) -> str:
    """Build http client."""
    return " ".join(value.split())
