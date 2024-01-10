#!/usr/bin/python3
""" N queens """

import sys


def is_safe(board, row, col):
    """ Check if a queen can be placed in the current position """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        """ All queens are placed successfully, print the solution """
        solutions.append([[i, board[i]] for i in range(n)])
    else:
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve_n_queens_util(board, row + 1, n, solutions)
                """ Backtrack """
                board[row] = -1


def solve_n_queens(n):
    """ Initialize an empty board """
    board = [-1] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


if __name__ == "__main__":
    """ Check the number of arguments """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        """ Parse the argument as an integer """
        n = int(sys.argv[1])

        """ Check if N is at least 4 """
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        """ Solve and print solutions """
        solutions = solve_n_queens(n)
        for solution in solutions:
            print(solution)

    except ValueError:
        print("N must be a number")
        sys.exit(1)
