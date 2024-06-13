"""File containing the class for the (hard coded) Function 3."""


# Import used classes
from classes.function import Function
from classes.vector import Vector
from classes.point import Point

class Function3(Function):
    """
    Function 3 of this project.

    The function is defined as follows: (x + 1)^2 + (y - 0,5)^2

    Attributes
    ----------
    intervals: list[Point]
        The two corner points of the interval of the function.

    Methods
    -------
    set_intervals
        Set the intervals of the function.
    get_intervals
        Return the intervals of the function.
    get_value
        Get the value of the gradient at a specified point.
    get_gradient
        Get the value of the gradient at a specified point.

    """

    def __init__(self, intervals: list[Point]) -> None:
        """
        Construct one object of the second function with the given parameters.

        Parameters
        ----------
        intervals: list[Point]
            The two corner points of the interval of the function.

        """
        super().__init__()
        self.set_intervals(intervals)

    def set_intervals(self, intervals: list[Point]) -> None:
        """
        Set the intervals of the function.

        Parameters
        ----------
        intervals: list[Point]
            The two corner points of the interval of the function.

        """
        self.__intervals: list[Point] = intervals

    def get_intervals(self) -> list[Point]:
        """
        Return the intervals of the function.

        Returns
        -------
        intervals: list[Point]
            The two corner points of the interval of the function.

        """
        return self.__intervals

    def get_value(self, x_value: float, y_value: float) -> float:
        """
        Calculate the value of a two dimensional function at a point.

        Parameters
        ----------
        x_value
            X value of the point.
        y_value: float
            Y value of the point.

        Returns
        -------
        float
            Value of the function at the specified point.

        """
        return (x_value + 1) ** 2 + (y_value - 0.5) ** 2

    def get_gradient(self, x_value: float, y_value: float) -> Vector:
        """
        Get the value of the gradient at a specified point.

        Parameters
        ----------
        x_value
            X value of the point.
        y_value: float
            Y value of the point.

        Returns
        -------
        Vector
            Values of the gradient at the specified point.

        """
        return Vector(2 * x_value + 2, 2 * y_value - 1)
