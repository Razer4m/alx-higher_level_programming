#!/usr/bin/python3
"""Solves the N queens problem."""

import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at the given position."""

    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, N):
    """Solve the N queens problem."""

    if col >= N:
        print_solution(board, N)
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            solve_nqueens(board, col + 1, N)

            board[i][col] = 0


def print_solution(board, N):
    """Print the solution."""
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print(f"{i}, {j}", end=" ")
    print()


def nqueens(N):
    """Solve the N queens problem."""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[0] * N for _ in range(N)]

    # Solve the N queens problem
    solve_nqueens(board, 0, N)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
