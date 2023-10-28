"""
A dummy module for showing how to use docstrings with sphinx.
"""

PI: float = 3.14159
"""Length of a circumference of diameter 1"""

HALF: float = 0.5
"""Half a unit"""


class IntResultsCalculator:
    """A calculator that only yields integer results

    It provides the following operations: add, subtract, multiply and divide.

    They all accept float args, but fail if the result is not an integer.
    """

    def __init__(self):
        pass

    def add(self, x: float, y: float = 0) -> int:
        """Sum two numbers (`x` + `y`).

        :param x: The first number to sum
        :param y: The second number to sum, defaults to 0
        :raises ValueError: if the result is not an integer
        :return: The sum of the two numbers
        """
        result = x + y

        # check if the result is an integer
        if result % 1 != 0:  # use modulus-1 to obtain the fractional part
            raise ValueError(f"{x} + {y} does not yield an integer result")

        return result

    def subtract(self, x: float, y: float = 0) -> int:
        """Subtract `y` from `x`.

        :param x: The number from which to subtract
        :param y: The number to be subtracted from `x`
        :raises ValueError: if the result is not an integer
        :return: The result of subtracting `y` from `x`
        """
        return self.sum(x, -y)  # reuse logic in add
