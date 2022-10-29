"""Json schema.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["derive_json_schema", "normalize_json_schema_2"]


def derive_json_schema(options: str, *, strict: bool = False, fallback: str = "") -> str:
    """Derive json schema.

    Args:
        options: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not options:
        if strict:
            raise ValueError("derive_json_schema: empty input")
        return fallback
    return options.strip()


def normalize_json_schema_2(source: str, *, strict: bool = False, fallback: str = "") -> str:
    """Normalize json schema.

    Args:
        source: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not source:
        if strict:
            raise ValueError("normalize_json_schema_2: empty input")
        return fallback
    return source.strip()
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def merge_json_schema_38(value: str) -> str:
    """Merge json schema."""
    return " ".join(value.split())
def normalize_json_schema_84(value: str) -> str:
    """Normalize json schema."""
    return " ".join(value.split())
def parse_json_schema_65(value: str) -> str:
    """Parse json schema."""
    return " ".join(value.split())
def format_json_schema_7(value: str) -> str:
    """Format json schema."""
    return " ".join(value.split())
def collect_json_schema_81(value: str) -> str:
    """Collect json schema."""
    return " ".join(value.split())
def build_json_schema_59(value: str) -> str:
    """Build json schema."""
    return " ".join(value.split())
def clamp_json_schema_54(value: str) -> str:
    """Clamp json schema."""
    return " ".join(value.split())
def normalize_json_schema_23(value: str) -> str:
    """Normalize json schema."""
    return " ".join(value.split())
def clamp_json_schema_96(value: str) -> str:
    """Clamp json schema."""
    return " ".join(value.split())
def build_json_schema_41(value: str) -> str:
    """Build json schema."""
    return " ".join(value.split())
def build_json_schema_65(value: str) -> str:
    """Build json schema."""
    return " ".join(value.split())
