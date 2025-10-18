"""
I did this one by hand, but might code a solution at some point. I did this by taking the prime factors of each number 1-20
and mapping each prime factor to its maximum number of occurences in any prime factorization. I then took the product of each
prime factor multiplied by its maximum number of occurences to get the answer.

[2, 2, 5], [19], [2, 3, 3], [17], [2, 2, 2, 2], [3, 5], [2, 7], [13], [2, 2, 3], [11], [2, 5], [3, 3], [2, 2, 2], [7], [2, 3], [5], [2, 2], [3], [2]

2: 4
3: 2
5: 1
7: 1
19: 1
17: 1
13: 1
11: 1

Answer = 2 * 2 * 2 * 2  * 3 * 3 * 5 * 7 * 19 * 17 * 13 * 11
"""
