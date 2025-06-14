""" tests/test_operations.py """
import pytest
from typing import Union
from app.operations import Operation

Number = Union[int, float]

@pytest.mark.parametrize(
        "x, y, expected",
        [
            (1, 2, 3),
            (-1, 2, 1),
            (-1, -2, -3),
            (1.5, 2.5, 4.0),
            (2.5, -1.5, 1.0),
            (-2.5, -3.0, -5.5),
        ],
        ids=[
            "add_positive",
            "add_mixed",
            "add_negative",
            "add_floats_positive",
            "add_floats_mixed",
            "add_floats_negative",
        ]
)
def test_add(x: Number, y: Number, expected: Number) -> None:
    """Test arithmetic 'add' from Operations."""
    result = Operations.add(x, y)
    assert result == expected, f"Expected {expected} from add({x}, {y}). Got {result}"

@pytest.mark.parametrize(
        "x, y, expected",
        [
            (3, 2, 1),
            (1, 2, -1),
            (-1, 2, -3),
            (-1, -2, 1),
            (2.5, 1.5, 1.0),
            (2.0, -1.5, 3.5),
            (-3.0, -2.0, -1.0),
        ],
        ids=[
            "subtract",
            "subtract_across_zero",
            "subtract_negative_base",
            "subtract_double_negative",
            "subtract_floats",
            "subtract_floats_inverted",
            "subtract_floats_double_negative",
        ]
)
def test_subtract(x: Number, y: Number, expected: Number) -> None:
    """Test arithmetic 'subtract' from Operations."""
    result = Operations.subtract(x, y)
    assert result == expected, f"Expected {expected} from subtract({x}, {y}). Got {result}"

@pytest.mark.parametrize(
        "x, y, expected",
        [
            (2, 4, 8),
            (-2, 4, -8),
            (-2, -4, 8),
            (2.0, 4.0, 8.0),
            (4.0, 0.5, 2.0),
            (-0.5, 4.0, -2.0),
            (-0.5, -0.5, 0.25),
        ],
        ids=[
            "multiply_positive",
            "multiply_mixed",
            "multiply_negative",
            "multiply_floats",
            "multiply_fractional_float",
            "multiply_floats_mixed",
            "multiply_floats_negative",
        ]
)
def test_multiplication(x: Number, y: Number, expected: Number) -> None:
    """Test arithmetic 'multiply' from Operations."""
    result = Operations.multiply(x, y)
    assert result == expected, f"Expected {expected} from multiply({x}, {y}). Got {result}"

@pytest.mark.parametrize(
        "x, y, expected",
        [
            (12, 6, 2),
            (-12, 4, -3),
            (12, -3, -4),
            (-12, -2, 6),
            (12.0, 1.0, 12.0),
            (12.0, 0.5, 24.0),
            (0.0, 12.0, 0.0),
        ],
        ids=[
            "divide_positive",
            "divide_negative_dividend",
            "divide_negative_divisor",
            "divide_all_negative",
            "divide_floats",
            "divide_fractional_divisor",
            "divide_zero_dividend",
        ]
)
def test_division(x: Number, y: Number, expected: Number) -> None:
    """Test arithmetic 'divide' from Operations"""
    result = Operations.divide(x, y)
    assert result == expected, f"Expected {expected} from divide({x}, {y}). Got {result}"
