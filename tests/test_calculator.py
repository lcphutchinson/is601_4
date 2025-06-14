""" tests/test_calculator.py """
import sys
from io import StringIO
from app.calculator.calculator import Calculator

def run_calculator_with_input(monkeypatch, inputs):
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator = Calculator()
    calculator.run()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()

def test_no_operands(monkeypatch):
    """Test non-exit REPL operation with no inputs"""
    inputs = ["add", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error:" in output

def test_one_operand(monkeypatch):
    """Test non-exit REPL operation with one input"""
    inputs = ["add 1", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error:" in output

def test_excess_operands(monkeypatch):
    """Test non-exit REPL operation with an excess of inputs"""
    inputs = ["add 3 4 5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error:" in output

def test_bad_operand(monkeypatch):
    """Test non-exit REPL operation with an invalid operand input"""
    inputs = ["add 1 2b", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error:" in output

def test_addition(monkeypatch):
    """Test valid REPL addition command"""
    inputs = ["add 5 6", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 11" in output
    assert "Error:" not in output

def test_subtraction(monkeypatch):
    """Test valid REPL subtraction command"""
    inputs = ["subtract 6 5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 1" in output
    assert "Error:" not in output

def test_multiplication(monkeypatch):
    """Test valid REPL multiplication command"""
    inputs = ["multiply 2 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 6" in output
    assert "Error:" not in output

def test_division(monkeypatch):
    """Test valid REPL division command"""
    inputs = ["divide 5 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 2.5" in output
    assert "Error:" not in output

def test_invalid_command(monkeypatch):
    inputs = ["nonsense 3 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error:" in output

def test_division_by_zero(monkeypatch):
    inputs = ["divide 2 0", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Error:" in output
