"""Rss feed.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["normalize_rss_feed"]


def normalize_rss_feed(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Normalize rss feed.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("normalize_rss_feed: empty input")
        return fallback
    return raw.strip()
def clamp_rss_feed_47(value: str) -> str:
    """Clamp rss feed."""
    return " ".join(value.split())
# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


# ... older helpers trimmed during refactor


def guard_rss_feed_65(value: str) -> str:
    """Guard rss feed."""
    return " ".join(value.split())
def format_rss_feed_18(value: str) -> str:
    """Format rss feed."""
    return " ".join(value.split())
def guard_rss_feed_40(value: str) -> str:
    """Guard rss feed."""
    return " ".join(value.split())
def derive_rss_feed_90(value: str) -> str:
    """Derive rss feed."""
    return " ".join(value.split())
def merge_rss_feed_71(value: str) -> str:
    """Merge rss feed."""
    return " ".join(value.split())
def guard_rss_feed_26(value: str) -> str:
    """Guard rss feed."""
    return " ".join(value.split())
def collect_rss_feed_10(value: str) -> str:
    """Collect rss feed."""
    return " ".join(value.split())
def ensure_rss_feed_33(value: str) -> str:
    """Ensure rss feed."""
    return " ".join(value.split())
