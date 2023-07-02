#!/usr/bin/python3
"""
The model contains the `pascal_triangle` function.
"""


def pascal_triangle(n):
    """
       `pascal_triangle` creates and return a list of
        list of integers representing the Pascal’s
        triangle of n.

        Agrs:
          n (integer): is height of the triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for row in range(n):
        curr_row = [1]  # Add 1 at the beginning of each row

        # Calculate the numbers in the middle of the row
        if row > 1:
            prev_row = triangle[row-1]
            for j in range(len(prev_row) - 1):
                curr_row.append(prev_row[j] + prev_row[j+1])

        # Add 1 at the end of each row
        if row > 0:
            curr_row.append(1)

        triangle.append(curr_row)

    return triangle
