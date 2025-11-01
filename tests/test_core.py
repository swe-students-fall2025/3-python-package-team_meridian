import pytest
from pyfortunecookie.core import get_fortune, get_lucky_number, get_color, get_tarot_reading, get_fortune_by_choice

def test_get_fortune():
    result = get_fortune()
    assert isinstance(result, str)
    assert len(result) > 0

def test_get_lucky_number():
    num = get_lucky_number()
    assert isinstance(num, int)
    assert 1 <= num <= 99

def test_get_color():
    color = get_color()
    assert isinstance(color, str)
    assert len(color) > 0

def test_get_tarot_reading_basic():
    text = get_tarot_reading()
    assert isinstance(text, str)
    assert ":" in text
    assert len(text) > 0

def test_get_tarot_reading_with_intent():
    text = get_tarot_reading(intent="needing_clarity")
    assert isinstance(text, str)
    assert ":" in text

def test_get_tarot_reading_invalid_intent_fallback():
    text = get_tarot_reading(intent="nonsense_value")
    assert isinstance(text, str)
    assert ":" in text

def test_get_fortune_by_choice_returns_dict():
        """Test that function returns a dictionary."""
        result = get_fortune_by_choice("fire", "dawn", "star")
        assert isinstance(result, dict)

def test_get_fortune_by_choice_has_required_keys():
        """Test that returned dict has all required keys."""
        result = get_fortune_by_choice("fire", "dawn", "star")
        required_keys = ["fortune", "element", "time", "symbol", "combination", "lucky_number", "lucky_color"]
        for key in required_keys:
            assert key in result

def test_get_fortune_by_choice_valid_elements():
        """Test all valid element choices."""
        elements = ["fire", "water", "earth", "air"]
        for element in elements:
            result = get_fortune_by_choice(element, "dawn", "star")
            assert result["element"] == element
            assert isinstance(result["fortune"], str)
            assert len(result["fortune"]) > 0