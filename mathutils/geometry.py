import math

def area_circle(radius):
    """
    Calculates the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def perimeter_circle(radius):
    """
    Calculates the perimeter (circumference) of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The perimeter (circumference) of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius
