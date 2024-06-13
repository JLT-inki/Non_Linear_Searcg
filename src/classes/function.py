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
        value: float
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

        Returns
        -------
        fibonacci_numbers.pop(): int
            The Nth Fibonacci number.

        """
        # check whether the desired number is one of the two starting numbers
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
            # Determine the gradient at the current position
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

    def fibonacci_search(self, number_of_steps: int, x_constant: bool,
                         current_point: Point) -> Point:
        """
        Use the Fibonacci Search to find a minimum.

        Parameters
        ----------
        number_of_steps: int
            The number of steps/calculations the method shall perform. This variable is
            also used to calculate the number of intervals and to calculate the
            starting point in the interval.
        x_constant: bool
            Boolean indicating which variable of the function is constant.
            If TRUE: The X variable is constant.
            If FALSE: The Y variable is constant.
        current_point: Point
            The current point that is used to get the constant X/Y value.

        Returns
        -------
        determined_point: Point
            Determined point of the minimum.

        """
        # Calculate the number of intervals (Fib[n + 2])
        number_of_intervals: int = Function.get_fibonacci_number(number_of_steps + 2)

        # Calculate the starting point (Fib[n])
        point_left: int = Function.get_fibonacci_number(number_of_steps)

        # Initialize the list containing all points on the interval
        points: list[Point] = []

        # Determine all points on the interval
        for i in range(number_of_intervals + 1):
            if x_constant:
                points.append(Point(
                    current_point.get_x_value(),
                    self.get_intervals()[0].get_y_value() + i / number_of_intervals *
                    abs(self.get_intervals()[1].get_y_value() -
                        self.get_intervals()[0].get_y_value())))
            else:
                points.append(Point(
                    self.get_intervals()[0].get_x_value() + i / number_of_intervals *
                    abs(self.get_intervals()[1].get_x_value() -
                        self.get_intervals()[0].get_x_value()),
                    current_point.get_y_value())
                )

        # Initialize the borders for the search as the interval of the function
        borders: tuple[int, int] = (0, number_of_intervals)

        # Initialize the right point
        point_right: int = number_of_intervals - point_left

        # Shrink the border from both sides until there is only one point left
        while borders[1] - borders[0] != 2:
            # Calculate the values of both points
            value_left = self.get_value(
                points[point_left].get_x_value(), points[point_left].get_y_value())
            value_right = self.get_value(
                points[point_right].get_x_value(), points[point_right].get_y_value())

            # Compare the two values and change the borders and points accordingly
            if value_left < value_right:
                borders = (borders[0], point_right)
                point_right = borders[1] - (point_left - borders[0])
            else:
                borders = (point_left, borders[1])
                point_left = borders[0] + (borders[1] - point_right)

            # Switch points if right < left to ensure the correctness
            if point_right < point_left:
                point_left, point_right = point_right, point_left

        # Return the point that sits between the two interval ends
        return points[borders[0] + 1]

    def edge_search(
            self, starting_point: Point, distance: float,
            number_of_steps: int) -> Point:
        """
        Use the edge search method to determine a minimum.

        Parameters
        ----------
        starting_point: Point
            Point from which the method starts.
        distance: float
            Distance in which two consecutive determined points need to be for the
            method to stop.
        number_of_steps: int
            The number of steps/calculations the method shall perform. This variable is
            also used to calculate the number of intervals and to calculate the
            starting point in the interval.

        Returns
        -------
        determined_point: Point
            Determined point of the minimum.

        """
        # Initialize the last determined point as the starting point
        last_point: Point = starting_point

        # initialize the boolean indicating which variable shall be constant
        x_constant: bool = True

        # Determine new points until two consecutive points are in range of one another
        while True:
            determined_point: Point = self.fibonacci_search(
                number_of_steps, x_constant, last_point)

            # Break the loop if two points are in range to one another
            if Point.points_are_in_range(last_point, determined_point, distance):
                break

            # Negate the boolean indicating which variable shall be constant
            x_constant = not x_constant

            # Update the last visited point
            last_point = determined_point

        return determined_point
