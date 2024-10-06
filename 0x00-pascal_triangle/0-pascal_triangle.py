#!/usr/bin/python3

"""
This module generates Pascal's Triangle up to a specified
number of levels using recursion.
"""


def recurse_column(triangle, start, stop):
    """
    Recursively generates and appends rows to Pascal's Triangle.

    Args:
        triangle (list): The current state of the triangle (list of lists).
        start (int): The current row index being processed.
        stop (int): The total number of rows to generate.

    Returns:
        list: The complete Pascal's Triangle with 'stop' rows.
    """
    if triangle.__len__() == stop or start == stop - 1:
        return triangle
    triangle.append(recurse_row(triangle, [], 0))
    recurse_column(triangle, start + 1, stop)
    return triangle


def recurse_row(triangle, new_row, start):
    """
    Recursively generates a new row for Pascal's Triangle
    based on the previous row.

    Args:
        triangle (list): The current state of the triangle.
        new_row (list): The row being constructed.
        start (int): The index of the element being processed
        in the current row.
        stop (int): The index of the row to generate.

    Returns:
        list: A completed row for Pascal's Triangle.
    """
    old_row = triangle[triangle.__len__() - 1]
    if start == 0 or old_row.__len__() == new_row.__len__():
        new_row.append(1)
    else:
        new_row.append(old_row[start - 1] + old_row[start])
    if triangle.__len__() == start:
        return new_row
    return recurse_row(triangle, new_row, start + 1)


def pascal_triangle(n):
    """
    Initializes the Pascal's Triangle and begins recursion
    to generate the full triangle.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: Pascal's Triangle with 'n' rows.
    """
    triangle = []
    if n < 1:
        return triangle
    return recurse_column([[1]], 0, n)
