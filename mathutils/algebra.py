 1c6feb1 (Added mathutils package, setup.py, and tests)
def solve_linear(a, b):
    """
    Solves a simple linear equation of the form ax + b = 0.
    
    Args:
        a (float): Coefficient of x.
        b (float): Constant term.

    Returns:
        float: Solution for x.

    Raises:
        ValueError: If 'a' is zero, as division by zero is not possible.
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")
    return -b / a
>>>>>>> 1c6feb1 (Added mathutils package, setup.py, and tests)
