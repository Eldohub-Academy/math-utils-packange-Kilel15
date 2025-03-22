<<<<<<< HEAD
import math

def area_circle(radius):
=======
<<<<<<< HEAD
# geometry.py - Calculate the area of basic shapes
import math

def area_circle(radius):
    """Returns the area of a circle given its radius."""
=======
import math

def area_circle(radius):
>>>>>>> 1c6feb1 (Added mathutils package, setup.py, and tests)
    """
    Calculates the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
<<<<<<< HEAD
=======
>>>>>>> cb3b38f (Added mathutils package, setup.py, and tests)
>>>>>>> 1c6feb1 (Added mathutils package, setup.py, and tests)
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

<<<<<<< HEAD
def perimeter_circle(radius):
    """
    Calculates the perimeter (circumference) of a circle given its radius.

=======
<<<<<<< HEAD
def area_square(side):
    """Returns the area of a square given its side length."""
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side ** 2

def area_rectangle(length, width):
    """Returns the area of a rectangle given its length and width."""
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return length * width
if __name__ == "__main__":    
    print("Area of a rectangle: ", area_rectangle(5, 3))  
    print("Area of a square: ", area_square(4)) 
    print("Area of a circle: ", area_circle(3))  
# The geometry.py module contains functions to calculate the area of basic shapes such as circles, squares, and rectangles. Each function takes the necessary parameters (e.g., radius, side length, length, width) and returns the calculated area. The module uses the math module to access the value of pi for circle calculations. The functions also include input validation to handle negative input values.
=======
def perimeter_circle(radius):
    """
    Calculates the perimeter (circumference) of a circle given its radius.

>>>>>>> 1c6feb1 (Added mathutils package, setup.py, and tests)
    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The perimeter (circumference) of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius
<<<<<<< HEAD
=======
>>>>>>> cb3b38f (Added mathutils package, setup.py, and tests)
>>>>>>> 1c6feb1 (Added mathutils package, setup.py, and tests)
