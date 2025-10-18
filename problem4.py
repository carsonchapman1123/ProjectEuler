from typing import List


def get_digits(n: int) -> List[int]:
    """
    Returns a list of digits of a number.
    """
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits


def is_palindrome(n: int) -> bool:
    """
    Takes a number and returns True if it is a palindrome.
    """
    digits = get_digits(n)
    for i in range(len(digits) // 2):
        if digits[i] != digits[-1 - i]:
            return False
    return True


def get_max_palindrome_product(n: int):
    """
    Returns the maximum palindromic product of two n digit numbers.
    """
    max_prod = 0
    f = 10 ** (n - 1)
    c = 10**n
    for x in range(f, c):
        for y in range(f, c):
            this = x * y
            if is_palindrome(this):
                max_prod = max(max_prod, this)
    return max_prod


print(get_max_palindrome_product(3))
