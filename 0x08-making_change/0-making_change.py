#!/usr/bin/python3
"""
Define `makeChange` function.
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a
       given amount total.

       Args:
          coins(list): values of the coins in your possession
          total(int): amount given.
    """
    if total <= 0:
        return 0

    # Sort the total descending
    coins.sort(reverse=True)
    number_of_coins = 0

    for coin in coins:
        count = total // coin
        remainder = total % coin

        if remainder == 0:
            number_of_coins += count
            return number_of_coins
        else:
            total = remainder
            number_of_coins += count
    return -1
