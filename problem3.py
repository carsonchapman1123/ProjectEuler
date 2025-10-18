from typing import List
import math

# Not including 2 here since we're only checking divisibility of odd numbers.
memo = [3]


def get_primes_up_to(n: int) -> List[int]:
    """
    Add prime numbers to memo up to n.
    """
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


n = 600851475143
get_primes_up_to(int(math.sqrt(n)))
for d in range(len(memo) - 1, 1, -1):
    if n % memo[d] == 0:
        print(memo[d])
