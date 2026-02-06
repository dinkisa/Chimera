def test_trend_structure():
    data = fetch_trends("youtube", "US")
    assert "trends" in data
    assert isinstance(data["trends"][0]["title"], str)
    assert isinstance(data["trends"][0]["views"], int)
