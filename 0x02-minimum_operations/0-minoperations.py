#!/usr/bin/python3
# This line specifies the interpreter to use for this script.

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
        # If n is 0, no operations are needed.
        return 0
    elif n == 1:
        # If n is 1, only one operation (Copy All) is needed.
        return 1

    # Recursively calculate the minimum number of
    # operations for n-1 and n/2 characters
    min_n_1 = minOperations(n-1)
    # Store the minimum operations for n-1 characters in a variable.
    min_n_2 = minOperations(n//2)
    # Store the minimum operations for n/2 characters in a variable.


    # Choose the minimum of the two options
    if n % 2 == 0:
        # If n is even
        return min(min_n_1 + 1, min_n_2 + 2)
    else:
        # If n is odd, only Option 1 is possible.
        return min_n_1 + 1

