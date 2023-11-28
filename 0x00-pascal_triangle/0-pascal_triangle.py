#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    - n (int): The number of rows to generate.

    Returns:
    - List[List[int]]: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    p_triangle = [[1]]

    for i in range(1, n):
        prev_row = p_triangle[i - 1]
        new_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)] + [1]
        p_triangle.append(new_row)

    return p_triangle