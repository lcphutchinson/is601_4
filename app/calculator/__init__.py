"""This module provides the primary REPL interface and handles all IO for the Calculator application"""

import sys
from app.calculation import Calculation, CalculationFactory

# Version string for the project: global only for ease of editing
version: str = "v.1.4"

def display_help() -> None:
    """Displays the command syntax and a list of valid operations, including examples."""
    help_message: str = """
Python Calculator REPL
----------------------
Usage:
    <command> <x> <y>
    - Perform an arithmetic calculation <command> on operands <x> and <y>
    - All operands must be float-parsible (integer or decimal)
    - Supported commands:
        add     : Adds two operands
        subtract: Subtracts operand <y> from <x>
        multiply: Multiplies two operands
        divide  : Divides operand <x> by <y>

Special Commands:
    exit    : Exit the calculator
    help    : Displays this help message
    history : Displays a calculation history for this session

Examples:
    add 2 3
    subtract 4.5 2
    multiply 3 4
    divide 12 6
    exit
    """
    print(help_message)

def display_history(history: list[Calculation]) -> None:
    """
    Displays the calculation history for this session.

    Parameters
    ----------
    history : List[calculation]
        A list of Calculation objects performed this session
    """
    if not history:
        print("Calculation history empty. Type 'help' for command information.")
    else:
        print("Calculation History")
        print("-------------------")
        for idx, calculation in enumerate(history, start=1):
            print(f"{idx}. {calculation}")

def calculator() -> None:
    """Launches the REPL"""
    
    history: list[Calculation] = []
    print(f"Welcome to Python REPL Calculator, {version}")
    print("Type 'help' for usage information or 'exit' to quit")

    while True:
        try:                                # Fetch the user input
            user_input = input(">>: ")
        except KeyboardInterrupt:           # Handle ctrl+c exit
            print("\nKeyboard interrupt detected. Exiting...")
            sys.exit(0)
        except EOFError:                    # Handle ctrl+d exit
            print("\nEOF detected. Exiting...")
            sys.exit(0)
        if not user_input:                  # Skip empty inputs
            continue # pragma: no cover
        match user_input.strip().split():
            case ["exit"]:
                print("Thank you for using Python REPL Calculator. Exiting...")
                break
            case ["help"]:
                display_help()
            case ["history"]:
                display_history(history)
            case [command, x, y]:
                try:                        # Parse inputs
                    calculation = CalculationFactory.create_calculation(command, x, y)
                except ValueError as e:     # Handle bad commands/operands
                    print(f"Error: {e}")
                    continue
                try:                        # Execute calculation
                    result = calculation.execute()
                except ZeroDivisionError:   # Handle zero divisor 
                    print("Error: divide <x> <y> requires non-zero divisor <y>")
                    continue
                except Exception as e:      # Handle unforseen errors
                    print(f"Unforseen Error: {e}")
                    sys.exit(0)

                result_str: str = f"{calculation}"
                print(f"Result: {result_str}")

                history.append(calculation)
            case _:                         # Handle bad input signatures
                print("Error: Invalid Command Syntax. Expected <command> <x> <y>.")

if __name__ == "__main__":
    calculator() # pragma: no cover
