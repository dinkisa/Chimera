"""Simple trend fetcher used by tests.

This minimal implementation returns a list of strings for supported
platforms and raises `ValueError` for unknown platforms so tests can
exercise both success and failure paths.
"""
from typing import List


def fetch_trends(platform: str) -> List[str]:
    platform = platform.lower()
    if platform not in ("twitter", "instagram"):
        raise ValueError(f"Unsupported platform: {platform}")
    # Return a small deterministic list suitable for tests
    if platform == "twitter":
        return ["#ExampleTrend", "#AnotherTrend"]
    return ["example_trend", "another_trend"]
