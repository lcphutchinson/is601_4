""" app/operation """

class Operation():
    """Stub Class for hosting static arithmetic methods"""

    @staticmethod
    def add(x: float, y: float) -> float:
        """
        Performs a two-operand addition

        Parameters
        ----------

        x : float
            First operand
        y : float
            Second operand

        Returns
        -------
        sum
            the sum of x and y
        """
        return x + y;

    @staticmethod
    def subtract(x: float, y: float) -> float:
        """
        Performs a two-operand subtraction

        Parameters
        ----------

        x : float
            Operand to be subtracted from
        y : float
            Operand to subtract

        Returns
        -------
        difference
            the difference of x and y
        """
        return x - y;

    @staticmethod
    def multiply(x: float, y: float) -> float:
        """
        Performs a two-operand multiplication

        Parameters
        ----------

        x : float
            First operand
        y : float
            Second operand

        Returns
        -------
        product
            the product of x and y
        """
        return x * y;

    @staticmethod
    def divide(x: float, y: float) -> float:
        """
        Performs a two-operand division

        Parameters
        ----------

        x : float
            Dividend operand
        y : float
            Divisor operand

        Returns
        -------
        quotient
            the quotient of x and y
        """
        return x / y;

