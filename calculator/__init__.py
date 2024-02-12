"""
Imports various modules and functions needed for the calculator. Defines a class with methods for performing arithmetic operations and managing calculations.
"""
from calculator.calculation import Calculation
from calculator.operations import Operations

class Calculator:
    '''Serves as a core componet of a basic calculator system. Integrates components for performing arithmetic calculations.'''

    def __init__(self):
        '''Initializes the Calculator with an instance of the Operations class'''
        self.operations = Operations()

    def perform_calculation(self, a, b, operation):
        '''Performs a operation with the given operands and operation, and returns the result'''
        calculation = Calculation(a, b, operation)
        return calculation.compute()
