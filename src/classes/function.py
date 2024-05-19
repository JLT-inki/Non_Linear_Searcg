"""File containing the abstract class Function."""

# Import Python libraries to make this class abstract and to overload its methods
from abc import ABC, abstractmethod

class Function(ABC):
    """
    Abstract class representing a function.

    Methods
    -------
    get_value
        Calculate the value of a two dimensional function at a specified position.
    get_fibonacci_number
        Get the Nth Fibonacci number.

    Notes
    -----
    This abstract class allows the creation of one, two and three dimensional
    functions.

    """

    @abstractmethod
    def get_value(self, x_value: float, y_value: float) -> float:
        ...

    @staticmethod
    def get_fibonacci_number(number: int) -> int:
        """
        Get the Nth Fibonacci number.

        Parameters
        ----------
        number: int
            The index of the Fibonacci number that shall be returned.

        Retuns
        ------
        fibonacci_numbers.pop(): int
            The Nth Fibonacci number.

        """
        # check wehteher the desired numebr is one of the two starting numbers
        if number <= 0:
            return 0
        if number == 1:
            return 1

        # Calculate the Fibonacci numbers
        fibonacci_numbers: list[int] = [0, 1]

        for i in range(2, number + 1):
            fibonacci_numbers.append(
                fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])

        return fibonacci_numbers.pop()
