"""File containing the class Point."""

# Import for points_are_in_range method
from __future__ import annotations

# Import used class
from classes.vector import Vector

class Point:
    """
    Class representing a (two dimensional) point.

    Attributes
    ----------
    x_value: float
        X value of the point.
    y_value: float
        Y value of the point.

    Methods
    -------
    set_x_value
        Set the X value of the point.
    set_y_value
        Set the Y value of the point.
    get_x_value
        Return the X value of the point.
    get_y_value
        Return the X value of the point.
    points_are_in_range
        Check if two points are within a specific range of each other.
    apply_vector
        Move a point according to a vector.

    """

    def __init__(self, x_value: int, y_value: int) -> None:
        """
        Construct one point with the given parameters.

        Parameters
        ----------
        x_value: float
            X value of the point.
        y_value: float
            Y value of the point.

        """
        self.set_x_value(x_value)
        self.set_y_value(y_value)

    def set_x_value(self, x_value: float) -> None:
        """
        Set the X value of the point.

        Parameters
        ----------
        x_value: float
            X value of the point.

        """
        self.x_value: float = x_value

    def set_y_value(self, y_value: float) -> None:
        """
        Set the Y value of the point.

        Parameters
        ----------
        y_value: float
            Y value of the point.

        """
        self.y_value: float = y_value

    def get_x_value(self) -> float:
        """
        Return the X value of the point.

        Returns
        -------
        x_value: float
            X value of the point.

        """
        return self.x_value

    def get_y_value(self) -> float:
        """
        Return the Y value of the point.

        Returns
        -------
        y_value: float
            Y value of the point.

        """
        return self.y_value

    @staticmethod
    def points_are_in_range(point_1: Point, point_2: Point, distance: float) -> bool:
        """
        Check if two points are within a specific range of each other.

        The calculation of the distance opf two points is done via the usage of the
        Pythagorean theorem.

        Parameters
        ----------
        point_1: Point
            First point of the check.
        point_2: Point
            Second point of the check.
        distance: float
            Distance in which the two points should be to one another.

        Returns
        -------
        bool:
            True if the two points are in range of one another, False otherwise.

        """
        return (((point_1.get_x_value() - point_2.get_x_value()) ** 2 +
                 (point_1.get_y_value() - point_2.get_y_value()) ** 2
                 ) ** .5 <= distance)

    def apply_vector(self, vector: Vector) -> None:
        """
        Move a point according to a vector.

        Parameters
        ----------
        vector: Vector
            Vector that is moved by.

        """
        # Apply the change to the X and Y variable
        self.set_x_value(self.get_x_value() + vector.get_x_value())
        self.set_y_value(self.get_y_value() + vector.get_y_value())
