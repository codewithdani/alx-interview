#!/usr/bin/python3
"""
 This line specifies the interpreter to use for this script.
"""


def minOperations(n):
    """ This function calculates the fewest number of
  operations needed to result in exactly
  n H characters in the file.

  Returns:
    the fewest number of operations needed,
    or 0 if n is impossible to achieve.
    """
    num_chars = 1  # chars in the file
    copy = 0  # how many H's copied
    operations_counter = 0  # operations counter

    while num_chars < n:
        # if did not copy anything yet
        if copy == 0:
            # copyall
            copy = num_chars
            # increment operations counter
            operations_counter += 1

        # if haven't pasted anything yet
        if num_chars == 1:
            # paste
            num_chars += copy
            # increment operations counter
            operations_counter += 1
            # continue to next loop
            continue

        remaining = n - num_chars  # remaining chars to Paste
        # check if impossible by checking if copy
        # has more than needed to reach the number desired
        # which also means num of chars in file is equal
        # or more than in the copy.
        # in both situations it's impossible to achieve n of chars
        if remaining < copy:
            return 0

        # if can't be devided
        if remaining % num_chars != 0:
            # paste current copy
            num_chars += copy
            # increment operations counter
            operations_counter += 1
        else:
            # copyall
            copy = num_chars
            # paste
            num_chars += copy
            # increment operations counter
            operations_counter += 2

    # if got the desired result
    if num_chars == n:
        return operations_counter
    else:
        return 0
