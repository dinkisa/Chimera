import pytest
# Assuming your trend fetching function is in a file called trend_fetcher.py
from trend_fetcher import fetch_trends

def test_fetch_trends_returns_correct_data_structure():
    trends = fetch_trends(platform="twitter")  # or "instagram"
    assert isinstance(trends, list)
    for trend in trends:
        assert isinstance(trend, str)

# This test is designed to FAIL initially
def test_fetch_trends_fails_when_platform_is_invalid():
    with pytest.raises(ValueError):
        fetch_trends(platform="invalid_platform")
