import pytest
from pyfortunecookie.core import get_fortune, get_lucky_number, get_color,get_tarot_reading

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


