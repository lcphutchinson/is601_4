""" app/calculation """

from abc import ABC, abstractmethod
from app.operation import Operation

class Calculation(ABC):

    def __init__(self, x: str, y: str) -> None:
        try:
            self.x: float = float(x)
            self.y: float = float(y)
        except ValueError as e:
            e.msg = "Operands <x>, <y> must be float-parsible"
            raise e

    @abstractmethod
    def execute(self) -> float:
        pass # pragma: no cover

    def __str__(self) -> str:
        result = self.execute()
        operation_name = self.__class__.__name__.replace('Calculation', '')
        return f"{self.__class__.__name__}: {self.x} {operation_name} {self.y} = {result}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

class CalculationFactory:
    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        def decorator(subclass):
            calculation_type_lower = calculation_type.lower()
            if calculation_type_lower in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            cls._calculations[calculation_type_lower] = subclass
            return subclass
        return decorator

    @classmethod
    def create_calculation(cls, calculation_type: str, x: str, y: str) -> Calculation:
        calculation_type_lower = calculation_type.lower()
        calculation_class = cls._calculations.get(calculation_type_lower)
        if not calculation_class:
            available_types = ', '.join(cls._calculations.keys())
            raise ValueError(f"Unsupported command: '{calculation_type}'. Available types: {available_types}")
        return calculation_class(x, y)

@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):
    def execute(self) -> float:
        return Operation.add(self.x, self.y)

@CalculationFactory.register_calculation('subtract')
class SubtractCalculation(Calculation):
    def execute(self) -> float:
        return Operation.subtract(self.x, self.y)

@CalculationFactory.register_calculation('multiply')
class MultiplyCalculation(Calculation):
    def execute(self) -> float:
        return Operation.multiply(self.x, self.y)

@CalculationFactory.register_calculation('divide')
class DivideCalculation(Calculation):
    def execute(self) -> float:
        if self.y == 0:
            raise ZeroDivisionError
        return Operation.divide(self.x, self.y)
