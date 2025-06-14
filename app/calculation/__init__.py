""" app/calculation """

from abc import ABC, abstractmethod
from app.operation import Operation

class Calculation(ABC):
    """Abstract Base Class for the Calculation family of classes."""
    def __init__(self, x: str, y: str) -> None:
        """
        Instantiates a Calculation from raw string inputs

        Parameters
        ----------
        x : str
            First operand input
        y : str
            Second operand input

        Raises
        ------
        ValueError
            If x or y are not float-parsible strings.
        """
        try:
            self.x: float = float(x)
            self.y: float = float(y)
        except ValueError as e:
            e.msg = "Operands <x>, <y> must be float-parsible"
            raise e

    @abstractmethod
    def execute(self) -> float:
        """
        Launches the class's underlying Operation.

        Must be implemented by child classes
        """
        pass # pragma: no cover

    def __str__(self) -> str:
        """
        Produces a string representation of a Calculation object.

        Includes subclass name, operands, and calculation result.

        Returns
        -------
        str
            A string representation of the Calculation
        """
        result = self.execute()
        operation_name = self.__class__.__name__.replace('Calculation', '')
        return f"{self.__class__.__name__}: {self.x} {operation_name} {self.y} = {result}"

    def __repr__(self) -> str:
        """
        Produces a more spartan string representation of a Calculation object, for debugging.

        Includes subclass name and operand values.

        Returns
        -------
        str
            A brief string representation of the Calculation
        """
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

class CalculationFactory:
    """Factory class for the Calculation family of classes"""
    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        """
        Decorator for registering Calculation subclasses to the CalculationFactory.

        Identifies each subclass with a unique string key

        Parameters
        ----------
        calculation_type : str
            The string key used to identify this calculation type.

        Raises
        ------
        ValueError
            When a calculation_type is passed that is already registered.
        """
        def decorator(subclass):
            calculation_type_lower = calculation_type.lower()
            if calculation_type_lower in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            cls._calculations[calculation_type_lower] = subclass
            return subclass
        return decorator

    @classmethod
    def create_calculation(cls, calculation_type: str, x: str, y: str) -> Calculation:
        """
        Factory method for instantiating Calculation subclasses

        Parameters
        ----------
        calculation_type : str
            A string denoting the calculation to undertake ('add', 'subtract', etc.)
        x : str
            First operand input to pass to the Calculation
        y : str
            Second operand input to pass to the Calculation

        Returns
        -------
        Calculation
            A child class of the subtype associatedw with calculation_type

        Raises
        ------
        ValueError
            When calculation_type does not correspond to a registered Calculation subclass.
        """
        calculation_type_lower = calculation_type.lower()
        calculation_class = cls._calculations.get(calculation_type_lower)
        if not calculation_class:
            available_types = ', '.join(cls._calculations.keys())
            raise ValueError(f"Unsupported command: '{calculation_type}'. Available types: {available_types}")
        return calculation_class(x, y)

@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):
    """Concrete Product class for addition operations"""
    def execute(self) -> float:
        """Performs an add operation on stored operands"""
        return Operation.add(self.x, self.y)

@CalculationFactory.register_calculation('subtract')
class SubtractCalculation(Calculation):
    """Concrete Product class for subtraction operations"""
    def execute(self) -> float:
        """Performs an subtract operation on stored operands"""
        return Operation.subtract(self.x, self.y)

@CalculationFactory.register_calculation('multiply')
class MultiplyCalculation(Calculation):
    """Concrete Product class for multiplication operations"""
    def execute(self) -> float:
        """Performs an multiply operation on stored operands"""
        return Operation.multiply(self.x, self.y)

@CalculationFactory.register_calculation('divide')
class DivideCalculation(Calculation):
    """Concrete Product class for division operations"""
    def execute(self) -> float:
        """
        Performs an divide operation on stored operands

        Raises
        ------
        ZeroDivisionError
            If the stored divisor operand is 0
        """
        if self.y == 0:
            raise ZeroDivisionError
        return Operation.divide(self.x, self.y)
