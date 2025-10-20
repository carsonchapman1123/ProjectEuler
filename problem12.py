import math


def count_divisors(n: int) -> int:
    """
    Count the number of divisors for a number n.
    """
    divs = set([1, n])
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            divs.add(d)
            divs.add(n // d)
    return len(divs)


def highly_divisible_triangular_number(n: int) -> int:
    """
    Searches for the first triangular number with over n divisors.
    """
    i = 1
    curr_num = 0
    while True:
        curr_num += i
        divs = count_divisors(curr_num)
        if divs > n:
            return curr_num
        i += 1


print(highly_divisible_triangular_number(500))
