#!/usr/bin/python3

def makeChange(coins, total):
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
