'''Tests Calculator class from __init__.py'''
# Disable specific pylint warnings that are not relevant for this file.
# pylint: disable=unnecessary-dunder-call, invalid-name
import pytest
from calculator import Calculator

@pytest.mark.parametrize("calculator_op, a, b, expected", [
    (Calculator.add, 2, 2, 4),
    (Calculator.subtract, 2, 2, 0),
    (Calculator.multiply, 2, 2, 4),
    (Calculator.divide, 2, 2, 1),
    (Calculator.divide, 6, 2, 3),
    (Calculator.divide, -1, -1, 1)
])
def test_calculator_operations(calculator_op, a, b, expected):
    '''Test Calculator class operations'''
    assert calculator_op(a, b) == expected, f"Failed {calculator_op.__name__} operation with {a} and {b}"

def test_calculator_divide_by_zero():
    '''Test calculator divide by zero exception'''
    with pytest.raises(ValueError):
        Calculator.divide(2, 0)
