def sum_of_multiples_of_3_or_5(n: int) -> int:
    """
    Returns the sum of all multiples of 3 or 5 up to the number n.
    """
    m3 = n // 3
    m5 = n // 5
    m15 = n // 15
    return (3 * m3 * (m3 + 1) + 5 * m5 * (m5 + 1) - 15 * m15 * (m15 + 1)) // 2


print(sum_of_multiples_of_3_or_5(999))
