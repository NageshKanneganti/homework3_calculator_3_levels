'''Tests operations.py'''
from calculator.operations import addition, subtraction, multiplication, division

# Test cases for operations.py"
def test_addition():
    '''Tests that addition function works'''
    assert addition(2,2) == 4

def test_subtraction():
    '''Tests that subtraction function works'''
    assert subtraction(2,2) == 0

def test_multiplication():
    '''Tests that multiplication function works'''
    assert multiplication(2,2) == 4

def test_division():
    '''Tests that division function works'''
    assert division(2,2) == 1
