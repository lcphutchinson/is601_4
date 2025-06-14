""" app/calculation """

from abc import ABC, abstractmethod
from app.operation import Operation

class Calculation(ABC):

    def __init__(self, x: str, y: str) -> None:

