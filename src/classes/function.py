"""File containing the abstract class Function."""

# Import Python libraries to make this class abstract
from abc import ABC, abstractmethod

# Import used classes
from classes.point import Point
from classes.vector import Vector

class Function(ABC):
    """
    Abstract class representing a (two dimensional) function.

    Methods
    -------
    get_value
        Calculate the value of a two dimensional function at a point.
    get_gradient
        Get the value of the gradient at a specified point.
    get_fibonacci_number
        Get the Nth Fibonacci number.
    gradient_descend
        Use the gradient descend method to determine a minimum.

    """

    @abstractmethod
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
        value: flaot
            Value of the function at the specified point.

        """

    @abstractmethod
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

    def gradient_descend(
            self, starting_point: Point, distance: float, factor: float) -> Point:
        """
        Use the gradient descend method to determine a minimum.

        Parameters
        ----------
        starting_point: Point
            Point from which the method starts.
        distance: float
            Distance in which two consecutive determined points need to be for the
            method to stop.
        factor: float
            Factor by which the point shall be moved by the vector.

        Returns
        -------
        determined_point: Point
            Determined point of the minimum.

        """
        # Initialize the last determined point as the starting point
        last_point: Point = starting_point

        # Determine new points until two consecutive points are in range of one another
        while True:
            # Deterine the gradient at the current position
            gradient: Vector = self.get_gradient(
                last_point.get_x_value(), last_point.get_y_value())

            # Normalize the gradient
            gradient.normalize()

            # Negate the values of the gradient
            gradient.negate_values()

            # Apply the gradient to the point
            determined_point: Point = last_point.apply_vector(gradient, factor)

            # Break the loop if two points are in range to one another
            if Point.points_are_in_range(last_point, determined_point, distance):
                break

            # Set the last determined point and continue the determination
            last_point = determined_point

        return determined_point
