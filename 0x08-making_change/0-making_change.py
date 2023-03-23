#!/usr/bin/python3

"""
Making Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total
    """
    # Initialize counter
    counter = 0

    # Initialize loop which stops when the total is equal to 0
    while(total > 0):
        array = []
        for coin in coins:
            if (coin <= total):
                array.append(coin)

        length = len(array)
        if(length == 0):
            return (-1)
        else:
            total = total - max(array)
            counter = counter + 1
    return counter
