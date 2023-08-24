#!/usr/bin/python3
"""
The Script to rotate a n x n 2D matrix, 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
      Rotate a n x n 2D matrix, 90 degrees clockwise.
    """
    lent = len(matrix[0])
    for i in range(lent // 2):
        for j in range(i, lent - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[lent - 1 - j][i]
            matrix[lent - 1 - j][i] = matrix[lent - 1 - i][lent - 1 - j]
            matrix[lent - 1 - i][lent - 1 - j] = matrix[j][lent - 1 - i]
            matrix[j][lent - 1 - i] = temp
