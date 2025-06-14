""" tests/test_calculator.py """
import pytest
import sys
from io import StringIO
from app.calculator import calculator
from app.calculation import CalculationFactory

def run_calculator_with_input(monkeypatch, inputs):
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()

def test_help(monkeypatch):
    """Tests the 'help' special command"""
    inputs = ["help", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Usage:" in output
    assert "Special Commands:" in output
    assert "Examples:" in output

def test_no_operands(monkeypatch):
    """Test non-exit REPL operation with no inputs"""
    inputs = ["add", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error: Invalid Command Syntax" in output

def test_one_operand(monkeypatch):
    """Test non-exit REPL operation with one input"""
    inputs = ["add 1", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error: Invalid Command Syntax" in output

def test_excess_operands(monkeypatch):
    """Test non-exit REPL operation with an excess of inputs"""
    inputs = ["add 3 4 5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error: Invalid Command Syntax" in output

def test_bad_operand(monkeypatch):
    """Test non-exit REPL operation with an invalid operand input"""
    inputs = ["add 1 2b", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error:" in output

def test_addition(monkeypatch):
    """Test valid REPL addition command"""
    inputs = ["add 5 6", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: AddCalculation: 5.0 Add 6.0 = 11.0" in output
    assert "Error:" not in output

def test_subtraction(monkeypatch):
    """Test valid REPL subtraction command"""
    inputs = ["subtract 6 5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: SubtractCalculation: 6.0 Subtract 5.0 = 1.0" in output
    assert "Error:" not in output

def test_multiplication(monkeypatch):
    """Test valid REPL multiplication command"""
    inputs = ["multiply 2 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: MultiplyCalculation: 2.0 Multiply 3.0 = 6.0" in output
    assert "Error:" not in output

def test_division(monkeypatch):
    """Test valid REPL division command"""
    inputs = ["divide 5 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: DivideCalculation: 5.0 Divide 2.0 = 2.5" in output
    assert "Error:" not in output

def test_division_by_zero(monkeypatch):
    inputs = ["divide 2 0", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error:" in output                              

def test_history_with_entries(monkeypatch):
    """Test the 'history' special command with recorded calculations"""
    inputs = ["add 5 6", "subtract 6 5", "history", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert """
Calculation History
-------------------
1. AddCalculation: 5.0 Add 6.0 = 11.0
2. SubtractCalculation: 6.0 Subtract 5.0 = 1.0
""" in output

def test_empty_history(monkeypatch):
    inputs = ["history", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Calculation history empty" in output

def test_invalid_command(monkeypatch):
    inputs = ["nonsense 3 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error:" in output

def test_keyboard_interrupt(monkeypatch):
    """Test exception handling for Keyboard Interrupt"""
    inputs = ["\x03"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Keyboard interrupt detected. Exiting..." in output

# Tests with capsys
def test_keyboard_interrupt(monkeypatch, capsys):
    def mock_input(prompt):
        raise KeyboardInterrupt()
    monkeypatch.setattr('builtins.input', mock_input)

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Keyboard interrupt detected. Exiting..." in captured.out

def test_EOF_input(monkeypatch, capsys):
    """Test exception handling for End-Of-File signal during input"""
    def mock_input(prompt):
        raise EOFError()
    monkeypatch.setattr('builtins.input', mock_input)

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "EOF detected. Exiting..." in captured.out

def test_unhandled_exception(monkeypatch, capsys):
    """Test explicitly unhandled exception during operation"""
    class MockCalculation:
        def execute(self):
            raise Exception("Mock exception during execution")
        def __str__(self):
            return "MockCalculation"

    def mock_create_calculation(operation, x, y):
        return MockCalculation()

    monkeypatch.setattr('app.calculation.CalculationFactory.create_calculation', \
                        mock_create_calculation)
    user_input = 'add 10 5\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Unforseen Error: Mock exception during execution" in captured.out
