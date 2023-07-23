#!/usr/bin/python3
"""
Defines the module `o-minoperation`.
"""


def minOperations(n):
    """
    A method that calculates the fewest number of operations
     needed to result in exactly n H characters in the file.

    Agrs:
        n (integer): The number used to increase `H`.

    Returns:
        Returns an integer.
    """
    if n <= 1:
        return 0  # No operations needed for n < 2

    # Initialize an integer to store the minimum operations
    operations = 0
    # Initialize an integer to store the prime factors of n
    prime = 2

    # Iterate untile `n <= 1`
    while n > 1:
        # If `prime` is a factor of `n`
        if n % prime == 0:
            operations += prime
            n //= prime  # returns the nearest whole number.
        else:
            # Else, increase prime by 1
            prime += 1

    return operations
