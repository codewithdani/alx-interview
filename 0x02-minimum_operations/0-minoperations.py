#!/usr/bin/python3

def minOperations(n):
    """
  This function calculates the fewest number of
  operations needed to result in exactly
  n H characters in the file.

  Returns:
    the fewest number of operations needed,
    or 0 if n is impossible to achieve.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursively calculate the minimum number of
    # operations for n-1 and n/2 characters
    min_n_1 = minOperations(n-1)
    min_n_/2 = minOperations(n//2)

    # Choose the minimum of the two options
    if n % 2 == 0:
        return min(min_n_1 + 1, min_n_/2 + 2)
    else:
        return min_n_1 + 1
