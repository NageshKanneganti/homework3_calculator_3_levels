'''Tests Calculator class from __init__.py'''
import pytest
from calculator import Calculator

def test_calculator_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2,2) == 4

def test_calculator_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(2,2) == 0

def test_calculator_multiplication():
    '''Test that division function works '''    
    assert Calculator.multiply(2,2) == 4

def test_calculator_division():
    '''Test that multiply function works '''    
    assert Calculator.divide(2,2) == 1

def test_calculator_divide_by_zero():
    '''Test calculator divide by zero exception'''
    with pytest.raises(ValueError):
        Calculator.divide(2,0)
