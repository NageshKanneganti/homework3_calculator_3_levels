'''Tests operations.py'''
from decimal import Decimal
import pytest
from calculator.operations import Operations as op

# Test cases for operations.py"
def test_operation_addition():
    '''Tests that addition function works'''
    assert op.addition(Decimal('2'), Decimal('3')) == Decimal('5')
    assert op.addition(Decimal('0.1'), Decimal('0.2')) == Decimal('0.3')

def test_operation_subtraction():
    '''Tests that subtraction function works'''
    assert op.subtraction(Decimal('5'), Decimal('3')) == Decimal('2')
    assert op.subtraction(Decimal('0.3'), Decimal('0.1')) == Decimal('0.2')

def test_operation_multiplication():
    '''Tests that multiplication function works'''
    assert op.multiplication(Decimal('2'), Decimal('3')) == Decimal('6')
    assert op.multiplication(Decimal('0.1'), Decimal('0.2')) == Decimal('0.02')

def test_operation_division():
    '''Tests that division function works'''
    assert op.division(Decimal('6'), Decimal('3')) == Decimal('2')
    assert op.division(Decimal('0.3'), Decimal('0.1')) == Decimal('3')

def test_operation_divide_by_zero():
    '''Test case for division by zero'''
    with pytest.raises(ValueError):
        op.division(Decimal('5'), Decimal('0'))
