#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a 2D grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island in the grid.

    Args:
        grid (list of list of int):
        The 2D grid representing water (0) and land (1).

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell
                # (to avoid double-counting edges)
                if i > 0 and grid[i - 1][j] == 1:  # Check above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
