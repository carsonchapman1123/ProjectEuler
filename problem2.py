import math

def nth_fibonacci(n: int) -> int:
    """
    Returns the nth fibonacci number.
    """
    return int((((1 + math.sqrt(5)) / 2)**n - ((1 - math.sqrt(5)) / 2)**n) / math.sqrt(5))

def sum_even_fibonacci(n: int) -> int:
    """
    Returns the sum of even fibonacci numbers up to n.

    This takes advantage of the fact that the (3 * x)th fibonacci number is
    even for any number x > 1.
    """
    s = 0
    curr_num = 3
    curr_fib = nth_fibonacci(curr_num)
    while curr_fib <= n:
        s += curr_fib
        curr_num += 3
        curr_fib = nth_fibonacci(curr_num)
    return s

print(sum_even_fibonacci(3999999))
