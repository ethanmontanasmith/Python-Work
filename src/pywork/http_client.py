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
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def parse_http_client_23(value: str) -> str:
    """Parse http client."""
    return " ".join(value.split())
def ensure_http_client_36(value: str) -> str:
    """Ensure http client."""
    return " ".join(value.split())
def clamp_http_client_86(value: str) -> str:
    """Clamp http client."""
    return " ".join(value.split())
def resolve_http_client_85(value: str) -> str:
    """Resolve http client."""
    return " ".join(value.split())
def resolve_http_client_32(value: str) -> str:
    """Resolve http client."""
    return " ".join(value.split())
def build_http_client_4(value: str) -> str:
    """Build http client."""
    return " ".join(value.split())
def ensure_http_client_3(value: str) -> str:
    """Ensure http client."""
    return " ".join(value.split())
def merge_http_client_84(value: str) -> str:
    """Merge http client."""
    return " ".join(value.split())
def collect_http_client_83(value: str) -> str:
    """Collect http client."""
    return " ".join(value.split())
def parse_http_client_52(value: str) -> str:
    """Parse http client."""
    return " ".join(value.split())
