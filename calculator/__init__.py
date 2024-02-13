"""
Imports various modules and functions needed for the calculator. Defines a class with methods for performing arithmetic operations and managing calculations.
"""
from decimal import Decimal
from typing import Callable
from calculator.calculation import Calculation
from calculator.operations import Operations as op
from calculator.calc_history import CalculationHistory as his

class Calculator:
    '''Serves as a core componet of a basic calculator system. Integrates components for performing arithmetic calculations and managing history.'''

    @staticmethod
    def _perform_calculation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        '''Performs a operation with the given operands and operation, and returns the result'''
        calculation = Calculation(a, b, operation)
        # Add the calculation to the history managed by the Calculations class
        his.add_calculation(calculation)
        return calculation.compute()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        '''Perform addition by delegating to the perform_calculation method with the addition operation'''
        return Calculator._perform_calculation(a, b, op.addition)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        '''Perform subtraction by delegating to the perform_calculation method with the addition operation'''
        return Calculator._perform_calculation(a, b, op.subtraction)

    @staticmethod
    def multiply (a: Decimal, b: Decimal) -> Decimal:
        '''Perform multiplication by delegating to the perform_calculation method with the addition operation'''
        return Calculator._perform_calculation(a, b, op.multiplication)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        '''Perform division by delegating to the perform_calculation method with the addition operation'''
        return Calculator._perform_calculation(a, b, op.division)
