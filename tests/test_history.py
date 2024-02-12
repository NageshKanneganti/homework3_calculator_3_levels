'''Tests calc_history.py'''
from decimal import Decimal
import pytest
from calculator.calc_history import CalculationHistory as his
from calculator.calculation import Calculation as calc
from calculator.operations import Operations as op

# Create a pytest envirioment
# Define pytest fixture to prepare the test environemnt for calculations
@pytest.fixture
def setup_calculations():
    '''Set up simple calculations to test calc_history.py'''
    # Clear history
    his.clear_history()
    # Add sample calculations to the history to set up a known state for testing
    his.add_calculation(calc(Decimal('10'), Decimal('5'), op.addition))
    his.add_calculation(calc(Decimal('20'), Decimal('3'), op.subtraction))

def test_add_calculation(setup_calculations):
    '''Tests that a calculation is added to history'''
    # Create a calculation object and add it to history
    new_calc = calc(Decimal('2'), Decimal('2'), op.addition)
    # Add the calculation to the history.
    his.add_calculation(new_calc)
    # Assert that the calculation was added to the history by checking if the latest calculation in the history matches the one we added.
    assert his.get_lastest_history() == new_calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    '''Test retrieving the entire calculation history'''
    # Retrieve the calculation history.
    history = his.get_history()
    # Assert that the history contains exactly 2 calculations, which matches our setup in the setup_calculations fixture.
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    '''Test clearing the entire calculation history'''
    # Clear the calculation history.
    his.clear_history()
    # Assert that the history is empty by checking its length.
    assert len(his.get_history()) == 0, "History was not cleared"

def test_get_latest_history(setup_calculations):
    '''Test getting the latest calculation from the history'''
    # Retrieve the latest calculation from the history.
    latest = his.get_lastest_history()
    # Assert that the latest calculation matches the expected values,
    # specifically the operands and operation used in the last added calculation
    # in the setup_calculations fixture.
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_get_latest_history_with_empty_history():
    '''Test getting the latest calculation when the history is empty'''
    # Ensure the history is empty by clearing it.
    his.clear_history()
    # Assert that the latest calculation is None since the history is empty.
    assert his.get_lastest_history() is None, "Expected None for latest calculation with empty history"
