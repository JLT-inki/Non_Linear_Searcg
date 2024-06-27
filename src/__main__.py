"""Main file of the project 'Non Linear Search'."""

# Import used Python libraries
import sys

# Import PI for function two
from math import pi

# Import used classes
from classes.function1 import Function1
from classes.function2 import Function2
from classes.function3 import Function3
from classes.vector import Vector
from classes.point import Point

# Global constants
# ====================================================================
# Starting point for both methods
STARTING_POINT: Point = Point(1.0, 1.0)
# Intervals for all three functions
INTERVALS: dict[int, list[Point]] = {
    1: [Point(-2.0, -2.0), Point(2.0, 2.0)],
    2: [Point(-5.0 * pi, -5.0 * pi), Point(5.0 * pi, 5.0 * pi)],
    3: [Point(-2.0, -2.0), Point(2.0, 2.0)]
}
# Constant indicating which method should be used
EDGE_SEARCH: bool = False


def main() -> int:
    """Execute the selected algorithm for the selected method."""
    # Initialize the function
    function: Function1 = Function1(INTERVALS[1])

    # Perform the actions needed for the selected method
    if EDGE_SEARCH:
        # Initialize the parameters used by the method
        distance: float = 0.01
        number_of_steps: int = 30

        # Execute the method
        found_min: Point = function.edge_search(
            STARTING_POINT, distance, number_of_steps)
    else:
        # Initialize the parameters used by the method
        distance: float = 0.01
        factor: float = 0.1

        # Execute the method
        found_min: Point = function.gradient_descend(
            STARTING_POINT, distance, factor)

    # Print the result
    print("The found minimum is at (", found_min.get_x_value(),
          ";", found_min.get_y_value(), ")")
    gradient: Vector = function.get_gradient(
        found_min.get_x_value(), found_min.get_y_value())
    print("Its gradient is (", gradient.get_x_value(), ";",
          gradient.get_y_value(), ")")

    # Return exitcode 0 indicating success
    return 0


if __name__ == "__main__":
    sys.exit(main())
