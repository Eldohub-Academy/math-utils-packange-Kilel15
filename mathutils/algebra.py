# algebra.py - Basic Algebraic Calculations

import math

def solve_linear(a, b):
    """Solves a simple linear equation ax + b = 0"""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")
    return -b / a

def gcd(a, b):
    """Finds the Greatest Common Divisor (GCD) using Euclidean Algorithm."""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """Finds the Least Common Multiple (LCM)."""
    if a == 0 or b == 0:
        raise ValueError("LCM of zero is undefined")
    return abs(a * b) // gcd(a, b)

def quadratic_roots(a, b, c):
    """Finds the roots of a quadratic equation ax^2 + bx + c = 0."""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2

def evaluate_polynomial(coeffs, x):
    """Evaluates a polynomial given a list of coefficients and a value of x.
    
    Example: If coefficients = [3, 2, 1] (representing 3x² + 2x + 1), 
    and x = 2, it calculates 3(2²) + 2(2) + 1.
    """
    result = 0
    degree = len(coefficients) - 1
    
    for coeff in coefficients:
        result += coeff * (x ** degree)
        degree -= 1
        return result

# Example usage
if __name__ == "__main__":
    print("Solving linear equation 2x + 3 = 0:", solve_linear(2, 3))
    print("GCD of 12 and 15:", gcd(12, 15))
    print("LCM of 12 and 15:", lcm(12, 15))
    print("Roots of quadratic equation x^2 - 5x + 6 = 0:", quadratic_roots(1, -5, 6))
    print("Evaluating polynomial 3x^2 + 2x + 1 at x=2:", evaluate_polynomial([3, 2, 1], 2))
