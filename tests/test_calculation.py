"""Tests calculation.py: tests that get_result method works as intended"""
# Disable specific pylint warnings that are not relevant for this file.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import Operations as op

# pytest.mark.parametrize decorator is used to parameterize a test function, enabling it to be called with different sets of arguments. Here, it's used to test various scenarios of arithmetic operations with both integer and decimal operands to ensure the operations work correctly under different conditions.
@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), op.addition, Decimal('15')),  # Test addition
    (Decimal('10'), Decimal('5'), op.subtraction, Decimal('5')),  # Test subtraction
    (Decimal('10'), Decimal('5'), op.multiplication, Decimal('50')),  # Test multiplication
    (Decimal('10'), Decimal('2'), op.division, Decimal('5')),  # Test division
    (Decimal('10.5'), Decimal('0.5'), op.addition, Decimal('11.0')),  # Test addition with decimals
    (Decimal('10.5'), Decimal('0.5'), op.subtraction, Decimal('10.0')),  # Test subtraction with decimals
    (Decimal('10.5'), Decimal('2'), op.multiplication, Decimal('21.0')),  # Test multiplication with decimals
    (Decimal('10'), Decimal('0.5'), op.division, Decimal('20')),  # Test division with decimals
])

def test_calculation_operation(a, b, operation, expected):
    '''
    Test calculation compute method with various scenarios.
    
    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    '''
    # Create a Calculation instance with the provided operands and operation.
    calc = Calculation(a, b, operation)
    # Perform the operation and assert that the result matches the expected value.
    assert calc.compute() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_divide_by_zero():
    '''Tests divide by zero exception'''
    with pytest.raises(ValueError):
        calc = Calculation(Decimal('5'), Decimal('0'), op.division)
        calc.compute()
