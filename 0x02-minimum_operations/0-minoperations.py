#!/usr/bin/python3
'''Minimum Operations challenge'''


def minOperations(n):
    ''' Calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    Returns an integer: If n is impossible to achieve, return 0 '''
    pasted = 1
    clipboard = 0
    counter = 0

    while pasted < n:
        # did not copy anything yet
        if clipboard == 0:
            clipboard = pasted
            counter += 1

        # haven't pasted anything yet
        if pasted == 1:
            pasted += clipboard
            counter += 1
            continue

        # remaining chars to paste
        remaining = n - pasted

        if remaining < clipboard:
            return 0

        if remaining % pasted != 0:
            # paste current clipboard
            pasted += clipboard
            counter += 1
        else:
            # copy all
            clipboard = pasted
            pasted += clipboard
            counter += 2

    # if desired result is gotten
    if pasted == n:
        return counter
    else:
        return 0
