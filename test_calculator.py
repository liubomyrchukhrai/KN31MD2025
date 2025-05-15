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

def test_chain_operations(calc):
    result = calc.add(3, 5)      # 8
    result = calc.multiply(result, 2)  # 16
    result = calc.subtract(result, 4)  # 12
    result = calc.divide(result, 2)    # 6.0
    assert result == 6.0

def test_sqrt(calc):
    assert calc.sqrt(4) == 2
    assert calc.sqrt(0) == 0
    assert calc.sqrt(1) == 1
    assert round(calc.sqrt(2), 5) == round(2 ** 0.5, 5)

def test_sqrt_negative(calc):
    with pytest.raises(ValueError, match="Cannot take square root of negative number."):
        calc.sqrt(-9)
