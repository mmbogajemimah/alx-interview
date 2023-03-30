#!/usr/bin/python3

'''
Island parameter
'''


def island_perimeter(grid):
    '''
    eturns the perimeter of the island described in grid
    '''
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # count top edge
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                # count bottom edge
                if row == rows - 1 or grid[row+1][col] == 0:
                    perimeter += 1
                # count left edge
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                # count right edge
                if col == cols - 1 or grid[row][col+1] == 0:
                    perimeter += 1
    return perimeter
