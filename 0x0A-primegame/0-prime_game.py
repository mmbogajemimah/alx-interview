#!/usr/bin/python3

'''
Prime Game
'''


def isWinner(x, nums):
    '''
    Returns who the winner of each game is.
    '''
    # Initialize variables
    winner = None
    maria_wins = 0
    ben_wins = 0

    # Iterate through each round
    for n in nums:
        # Generate list of primes up to n
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        primes = [i for i in range(n + 1) if primes[i]]

        # Play the game
        player = "Maria"
        while primes:
            # Choose a prime and remove its multiples
            if player == "Maria":
                for p in primes:
                    if p <= n:
                        primes = [x for x in primes if x % p != 0 or x == p]
                        break
                else:
                    # Ben wins
                    ben_wins += 1
                    break
                player = "Ben"
            else:
                for p in primes:
                    if p <= n:
                        primes = [x for x in primes if x % p != 0 or x == p]
                        break
                else:
                    # Maria wins
                    maria_wins += 1
                    break
                player = "Maria"

        # Update winner
        if maria_wins > ben_wins:
            winner = "Maria"
        elif ben_wins > maria_wins:
            winner = "Ben"

    # Return winner
    return winner
