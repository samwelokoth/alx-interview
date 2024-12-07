#!/usr/bin/python3

"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """Returns the perimeter of the
    island described in grid"""

    number_of_rows = len(grid)
    number_of_columns = len(grid[0])

    perimeter = 0

    for x in range(number_of_rows):
        for y in range(number_of_columns):
            if grid[x][y] == 1:
                perimeter += 4
                if x != 0 and grid[x - 1][y] == 1:
                    perimeter -= 2
                if y != 0 and grid[x][y - 1] == 1:
                    perimeter -= 2
    return perimeter
