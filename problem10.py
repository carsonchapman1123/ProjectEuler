from typing import List
import math

# Not including 2 here since we're only checking divisibility of odd numbers.
memo = [3]


def sum_primes_up_to(n: int) -> List[int]:
    """
    Add prime numbers to memo up to n and sum each one added.
    """
    if n == 1:
        return 0
    if n == 2:
        return 2
    s = 5
    for i in range(5, n + 1, 2):
        j = 0
        sqrti = math.sqrt(i)
        divisible = False
        while memo[j] <= sqrti:
            if i % memo[j] == 0:
                divisible = True
                break
            j += 1
        if not divisible:
            memo.append(i)
            s += i
    return s


print(sum_primes_up_to(1999999))
