import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    # Arrange (Förbered)
    a = 2
    b = 3
    
    # Act (Utför)
    result = add(a, b)
    
    # Assert (Kontrollera)
    assert result == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # Testar att rätt exception kastas
    with pytest.raises(ValueError, match="Kan inte dividera med noll!"):
        divide(10, 0)