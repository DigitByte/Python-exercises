def equilateral(sides):
    # A triangle is equilateral if all three sides are equal.
    # First, check that the triangle is valid
    if not is_valid_triangle(sides):
        return False
    # All three sides must be the same
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    # A triangle is isosceles if at least two sides are the same.
    if not is_valid_triangle(sides):
        return False
    # Check if any two sides are equal
    a, b, c = sides
    return a == b or b == c or a == c


def scalene(sides):
    # A triangle is scalene if all three sides are different.
    if not is_valid_triangle(sides):
        return False
    # Check if all sides are different
    a, b, c = sides
    return a != b and b != c and a != c


def is_valid_triangle(sides):
    # Check if the triangle is valid based on two conditions:
    # 1. All sides must be greater than 0
    # 2. The sum of the lengths of any two sides must be
    #    greater than or equal to the third side
    a, b, c = sides

    # Check all sides are positive numbers
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Check triangle inequality
    return (a + b >= c) and (b + c >= a) and (a + c >= b)
