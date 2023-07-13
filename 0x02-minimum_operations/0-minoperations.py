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

    # Initialize a list to store the minimum operations for
    # each index
    dp = [float('inf')] * (n + 1)
    # Base case: No operations needed for n < 2
    dp[1] = 0

    # The outer loop iterates from 2 to n
    for i in range(2, n + 1):
        #  The inner loop iterates from 1 to i - 1
        # and checks if i is divisible by j.
        for j in range(1, i):
            if i % j == 0:
                # If it is, We update the minimum operations
                # using min(dp[i], dp[j] + i // j).
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
