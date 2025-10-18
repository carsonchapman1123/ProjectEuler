def square_of_sum_minus_sum_of_squares(n):
    """
    Returns the difference between the square of sum and sum of squares up to a number n.
    Derived using their respective formulas.
    """
    return ((3 * n * n * (n + 1) * (n + 1)) - (2 * (n * n + n) * (2 * n + 1))) // 12


print(square_of_sum_minus_sum_of_squares(100))
