""" tests/test_calculations """

import pytest
from unittest.mock import patch
from app.operation import Operation
from app.calculation import (
        CalculationFactory,
        AddCalculation,
        SubtractCalculation,
        MultiplyCalculation,
        DivideCalculation,
        Calculation
)

@patch.object(Operation, 'add')
def test_add_execute(mock_addition):
    """Tests the execute method of the AddCalculation subclass"""
    x = 2
    y = 4
    expected_result = 6
    mock_addition.return_value = expected_result
    add_calc = AddCalculation(x, y)

    result = add_calc.execute()

    mock_addition.assert_called_once_with(x, y)
    assert result == expected_result

@patch.object(Operation, 'add')
def test_add_exception(mock_addition):
    """Tests error handling in the case of an exception during AddCalculation.execute()"""
    x = 2
    y = 4
    mock_addition.side_effect = Exception("Addition error")
    add_calc = AddCalculation(x, y)

    with pytest.raises(Exception) as exc_info:
        add_calc.execute()

    assert str(exc_info.value) == "Addition error"

@patch.object(Operation, 'subtract')
def test_subtract_exception(mock_subtraction):
    """Tests the execute method of the SubtractCalculation subclass"""
    x = 6
    y = 4
    expected_result = 2
    mock_subtraction.return_value = expected_result
    subtract_calc = SubtractCalculation(x, y)

    result = subtract_calc.execute()

    mock_subtraction.assert_called_once_with(x, y)
    assert result == expected_result

@patch.object(Operation, 'subtract')
def test_subtract_exception(mock_subtraction):
    """Tests error handling in the case of an exception during SubtractCalculation.execute()"""
    x = 6
    y = 4
    mock_subtraction.side_effect = Exception("Subtraction error")
    subtract_calc = SubtractCalculation(x, y)

    with pytest.raises(Exception) as exc_info:
        subtract_calc.execute()

    assert str(exc_info.value) == "Subtraction error"

@patch.object(Operation, 'multiply')
def test_multiply_execute(mock_multiplication):
    """Tests the execute method of the MultiplyCalculation subclass"""
    x = 2
    y = 4
    expected_result = 8
    mock_multiplication.return_value = expected_result
    multiply_calc = MultiplyCalculation(x, y)

    result = multiply_calc.execute()

    mock_multiplication.assert_called_once_with(x, y)
    assert result == expected_result

@patch.object(Operation, 'multiply')
def test_multiply_exception(mock_multiplication):
    """Tests error handling in the case of an exception during MultiplyCalculation.execute()"""
    x = 2
    y = 4
    mock_multiplication.side_effect = Exception("Multiplication error")
    multiply_calc = MultiplyCalculation(x, y)

    with pytest.raises(Exception) as exc_info:
        multiply_calc.execute()

    assert str(exc_info.value) == "Multiplication error"

@patch.object(Operation, 'divide')
def test_divide_execute(mock_division):
    """Tests the execute method of the DivideCalculation subclass"""
    x = 8
    y = 4
    expected_result = 2
    mock_division.return_value = expected_result
    divide_calc = DivideCalculation(x, y)

    result = divide_calc.execute()

    mock_division.assert_called_once_with(x, y)
    assert result == expected_result

@patch.object(Operation, 'divide')
def test_divide_exception(mock_division):
    """Tests error handling in the case of an exception during DivideCalculation.execute()"""
    x = 8
    y = 4
    mock_division.side_effect = Exception("Division error")
    divide_calc = DivideCalculation(x, y)

    with pytest.raises(Exception) as exc_info:
        divide_calc.execute()

    assert str(exc_info.value) == "Division error"

def test_divide_by_zero():
    x = 8
    y = 0
    divide_calc = DivideCalculation(x, y)

    with pytest.raises(ZeroDivisionError) as exc_info:
        divide_calc.execute()

    assert str(exc_info.value) == ""

# Factory Tests

def test_create_add():
    """Test factory creation of an AddCalculation object"""
    x = 2
    y = 3

    calc = CalculationFactory.create_calculation('add', x, y)

    assert isinstance(calc, AddCalculation)
    assert calc.x == x
    assert calc.y == y

def test_create_subtract():
    """Test factory creation of a SubtractCalculation object"""
    x = 3
    y = 2

    calc = CalculationFactory.create_calculation('subtract', x, y)

    assert isinstance(calc, SubtractCalculation)
    assert calc.x == x
    assert calc.y == y

def test_create_multiply():
    """Test factory creation of a MultiplyCalculation object"""
    x = 2
    y = 3

    calc = CalculationFactory.create_calculation('multiply', x, y)

    assert isinstance(calc, MultiplyCalculation)
    assert calc.x == x
    assert calc.y == y

def test_create_divide():
    """Test factory creation of a DivideCalculation object"""
    x = 6
    y = 3

    calc = CalculationFactory.create_calculation('divide', x, y)
    assert calc.x == x
    assert calc.y == y

def test_create_unsupported():
    """Test error handling for unsupported command entry"""
    x = 2
    y = 3
    unsupported_type = 'factorial'

    with pytest.raises(ValueError) as exc_info:
        CalculationFactory.create_calculation(unsupported_type, x, y)

    assert f"Unsupported command: '{unsupported_type}'" in str(exc_info.value)

def test_register_duplicate():
    """Test error handling of duplicate subclass registration"""
    with pytest.raises(ValueError) as exc_info:
        @CalculationFactory.register_calculation('add')
        class AnotherAddCalculation(Calculation):
            """Duplicate registration of the Addition operation"""
            def execute(self) -> float:
                return Operation.add(self.x, self.y)

    assert "Calculation type 'add' is already registered." in str(exc_info.value)

# toString tests
# note -- these methods belong to Calculation. I'm not testing every subclass when none modify the method"

@patch.object(Operation, 'add', return_value=5.0)
def test_str_method(mock_addition):
    """Tests Calculation.__str__ method using an AddCalculation"""
    x = "2"
    y = "3"
    add_calc = AddCalculation(x, y)

    calc_str = str(add_calc)

    expected_str = f"{add_calc.__class__.__name__}: {float(x)} Add {float(y)} = 5.0"
    assert calc_str == expected_str

def test_repr_method():
    """Tests Calculation.__repr__ method using an AddCalculation"""
    x = 2
    y = 3
    add_calc = AddCalculation(x, y)

    calc_repr = repr(add_calc)

    expected_repr = f"{AddCalculation.__name__}(x={float(x)}, y={float(y)})"
    assert calc_repr == expected_repr

# parameterized tests
# note -- there is no coverage gap here, but this is required for the assignment

@pytest.mark.parametrize("calc_type, x, y, expected_result", [
    ('add', -5, 10.2, 5.2),
    ('subtract', 0, 12.0, -12.0),
    ('multiply', 0, 5, 0.0),
    ('divide', 4, 0.25, 16.0),
])
@patch.object(Operation, 'add')
@patch.object(Operation, 'subtract')
@patch.object(Operation, 'multiply')
@patch.object(Operation, 'divide')
def test_execute_parameterized(
        mock_division, mock_multiplication, mock_subtraction, mock_addition,
        calc_type, x, y, expected_result
):
    """Parameterized test for the execute method across Calculation subclasses"""
    match calc_type:
        case 'add':
            mock = mock_addition
        case 'subtract':
            mock = mock_subtraction
        case 'multiply':
            mock = mock_multiplication
        case 'divide':
            mock = mock_division
    mock.return_value = expected_result

    calc = CalculationFactory.create_calculation(calc_type, x, y)
    result = calc.execute()

    mock.assert_called_once_with(x, y)
    assert result == expected_result
