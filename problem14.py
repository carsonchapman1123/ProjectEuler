def collatz_length(n: int) -> int:
    """
    Returns the length of the collatz sequence starting at a number n.
    """
    cnt = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        cnt += 1
    return cnt


def longest_collatz(n: int) -> int:
    """
    Returns the longest collatz sequence using starting numbers up to n.
    """
    max_len = 0
    max_start = 0
    for i in range(1, n + 1):
        this_len = collatz_length(i)
        if this_len > max_len:
            max_len = this_len
            max_start = i
    return max_start


print(longest_collatz(1000000))
