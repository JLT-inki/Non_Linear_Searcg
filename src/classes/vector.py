"""File containing the class Vector."""

class Vector:
    """
    Class representing a (two dimensional) vector.

    Attributes
    ----------
    x_value: float
        X value of the vector.
    y_value: float
        Y value of the vector.

    Methods
    -------
    set_x_value
        Set the X value of the vector.
    set_y_value
        Set the Y value of the vector.
    get_x_value
        Return the X value of the vector.
    get_y_value
        Return the X value of the vector.
    normalize
        Normalize the vector, aka making its length equal to 1.
    negate_values
        Negate all the values of the vector.

    """

    def __init__(self, x_value: int, y_value: int) -> None:
        """
        Construct one vector with the given parameters.

        Parameters
        ----------
        x_value: float
            X value of the vector.
        y_value: float
            Y value of the vector.

        """
        self.set_x_value(x_value)
        self.set_y_value(y_value)

    def set_x_value(self, x_value: float) -> None:
        """
        Set the X value of the vector.

        Parameters
        ----------
        x_value: float
            X value of the vector.

        """
        self.__x_value: float = x_value

    def set_y_value(self, y_value: float) -> None:
        """
        Set the Y value of the vector.

        Parameters
        ----------
        y_value: float
            Y value of the vector.

        """
        self.__y_value: float = y_value

    def get_x_value(self) -> float:
        """
        Return the X value of the vector.

        Returns
        -------
        x_value: float
            X value of the vector.

        """
        return self.__x_value

    def get_y_value(self) -> float:
        """
        Return the Y value of the vector.

        Returns
        -------
        y_value: float
            Y value of the vector.

        """
        return self.__y_value

    def normalize(self) -> None:
        """Normalize the vector, aka making its length equal to 1."""
        # Calculate the factor to normalize the vector
        factor: float = 1 / (self.get_x_value() ** 2 + self.get_y_value() ** 2) ** .5

        # Apply the factor to all elements of the vector
        self.set_x_value(self.get_x_value() * factor)
        self.set_y_value(self.get_y_value() * factor)

    def negate_values(self) -> None:
        """Negate all the values of the vector."""
        self.set_x_value(-1 * self.get_x_value())
        self.set_y_value(-1 * self.get_y_value())
