"""Tests calculation.py: tests that get_result method works as intended"""
# Disable specific pylint warnings that are not relevant for this file.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import Operations as op

# pytest.mark.parametrize decorator is used to parameterize a test function, enabling it to be called with different sets of arguments. Here, it's used to test various scenarios of arithmetic operations with both integer and decimal operands to ensure the operations work correctly under different conditions.
@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('2'), Decimal('2'), op.addition, Decimal('4')),  # Test addition
    (Decimal('2'), Decimal('2'), op.subtraction, Decimal('0.0')),  # Test subtraction
    (Decimal('2'), Decimal('2'), op.multiplication, Decimal('4.0')),  # Test multiplication
    (Decimal('2'), Decimal('2'), op.division, Decimal('1.0')),  # Test division
    (Decimal('2.5'), Decimal('0.5'), op.addition, Decimal('3.0')),  # Test addition with decimals
    (Decimal('2.5'), Decimal('0.5'), op.subtraction, Decimal('2.0')),  # Test subtraction with decimals
    (Decimal('2.5'), Decimal('2.0'), op.multiplication, Decimal('5.0')),  # Test multiplication with decimals
    (Decimal('2.5'), Decimal('0.5'), op.division, Decimal('5.0')),  # Test division with decimals
])

def test_calculation_operations(a, b, operation, expected):
    ''' Test calculation compute method with various scenarios'''
    # Create a Calculation instance with the operands and operations from parametrized test data.
    calc = Calculation.create_calculation(a, b, operation)
    # Assert if the actual output from compute method matches expected from parameterized test data.
    assert calc.compute() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_divide_by_zero():
    '''Tests divide by zero exception'''
    with pytest.raises(ValueError):
        calc = Calculation(Decimal('5'), Decimal('0'), op.division)
        calc.compute()

def test_calculation_string_representation():
    '''Test __repr__ of Calculation class. Determines if string representation is accurate.'''
    # Create calculation instance
    str_rep = Calculation(Decimal('10'), Decimal('5'), op.addition)
    # Define expected string representation
    expected_rep = "Calculation(10, 5, addition)"
    # Assert that the actual output matches the expected output
    assert str_rep.__repr__() == expected_rep, "The __repr__ method output does not match the expected string"
