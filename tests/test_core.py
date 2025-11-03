import pytest
from pyfortunecookie.core import get_fortune, get_lucky_number, get_color,get_tarot_reading, get_rune_reading

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

def test_get_rune_reading_correct_format():
    rng = random.Random(42)
    result = get_rune_reading(n=3, rng=rng)
    assert isinstance(result, list)
    assert len(result) == 3
    assert all(isinstance(r, str) for r in result)
    assert all(":" in r for r in result)

def test_get_rune_reading_uniqueness():
    a = random.Random(100)
    b = random.Random(100)
    ra = get_rune_reading(n=3, rng=a)
    rb = get_rune_reading(n=3, rng=b)
    assert ra == rb

def test_get_rune_reading_invalid_n():
    with pytest.raises(ValueError):
        get_rune_reading(n=0)