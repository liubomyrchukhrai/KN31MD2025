import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(3, 4) == 7
    assert calc.add(-1, -2) == -3
    assert calc.add(0, 0) == 0

def test_subtract(calc):
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(-1, -1) == 0
    assert calc.subtract(0, 5) == -5

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-1, 5) == -5
    assert calc.multiply(0, 100) == 0

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(-9, 3) == -3
    assert calc.divide(7, 2) == 3.5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(10, 0)
        
def test_invalid_input_add(calc):
    with pytest.raises(TypeError):
        calc.add("a", 5)

def test_invalid_input_divide(calc):
    with pytest.raises(TypeError):
        calc.divide(10, "b")

def test_modulus(calc):
    assert calc.modulus(10, 3) == 1
    assert calc.modulus(9, 3) == 0
    assert calc.modulus(-10, 3) == 2   
    assert calc.modulus(10, -3) == -2

def test_modulus_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.modulus(10, 0)

def test_chained_operations(calc):
    result = calc.multiply(calc.add(2, 3), 4) 
    assert result == 20

def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(2, -2) == 0.25
    assert calc.power(-3, 3) == -27

def test_average(self):
    assert calc.average(4, 6) == 5

