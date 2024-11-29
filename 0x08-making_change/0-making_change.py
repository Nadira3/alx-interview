#!/usr/bin/python3
""" Greedy algorithms implementation """


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations.
        total (int): Target amount.

    Returns:
        int: Minimum number of coins required to make up the total.
             Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be met with the available coins.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        # Use as many of the current coin as possible
        count += total // coin
        total %= coin

    return count if total == 0 else -1
