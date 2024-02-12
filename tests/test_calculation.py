"""Tests calculation.py: tests that get_result method works as intended"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import Operations as op

# Tests cases for Calculation class
def test_calculation_addition():
    '''Tests addition operation works'''
    calc = Calculation(Decimal('2'), Decimal('3'), op.addition)
    assert calc.compute() == Decimal('5')

def test_calculation_subtraction():
    '''Tests subtraction operation works'''
    calc = Calculation(Decimal('5'), Decimal('3'), op.subtraction)
    assert calc.compute() == Decimal('2')

def test_calculation_multiplication():
    '''Tests multiplication operation works'''
    calc = Calculation(Decimal('2'), Decimal('3'), op.multiplication)
    assert calc.compute() == Decimal('6')

def test_calculation_division():
    '''Tests division operation works'''
    calc = Calculation(Decimal('6'), Decimal('3'), op.division)
    assert calc.compute() == Decimal('2')

def test_calculation_divide_by_zero():
    '''Tests divide by zero exception'''
    with pytest.raises(ValueError):
        calc = Calculation(Decimal('5'), Decimal('0'), op.division)
        calc.compute()()
