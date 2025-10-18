from typing import List
import math

# Not adding 2 to the memo since we're checking divisiblity of odd numbers.
memo = [3]


def get_nth_prime(n: int) -> List[int]:
    """
    Returns the nth prime number.
    """
    if n == 1:
        return 2
    i = 5
    while len(memo) < n - 1:
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
        i += 2
    return memo[-1]


print(get_nth_prime(10001))
