#!/usr/bin/python3
"""
Define the module `0-island_perimeter`
"""


def island_perimeter(grid):
    """The function calculate and returns the perimeter of the
       island described in the grid.

       Args:
         grid (list) - list of list of integers
    """

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                perimeter += 4  # Start with 4 sides

                # Check adjacent cells (up, down, left, and right)
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2  # Subtract 2 if adjacent cell is land
                if r > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2  # Subtract 2 if adjacent cell is land

    return perimeter
