#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.
"""

import sys

def initialize_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def board_copy(board):
    """Return a copy of a chessboard."""
    return [row.copy() for row in board]

def find_queen_positions(board):
    """Return the list of queen positions on the chessboard."""
    queens = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                queens.append([r, c])
    return queens

def mark_attacked_positions(board, row, col):
    """Mark attacked positions on the chessboard."""
    n = len(board)
    for i in range(n):
        board[row][i] = 'x'
        board[i][col] = 'x'
        if 0 <= row + i < n and 0 <= col + i < n:
            board[row + i][col + i] = 'x'
        if 0 <= row + i < n and 0 <= col - i < n:
            board[row + i][col - i] = 'x'
        if 0 <= row - i < n and 0 <= col + i < n:
            board[row - i][col + i] = 'x'
        if 0 <= row - i < n and 0 <= col - i < n:
            board[row - i][col - i] = 'x'

def solve_nqueens(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(find_queen_positions(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = board_copy(board)
            tmp_board[row][col] = "Q"
            mark_attacked_positions(tmp_board, row, col)
            solutions = solve_nqueens(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board_size = int(sys.argv[1])
    chessboard = initialize_board(board_size)
    solutions = solve_nqueens(chessboard, 0, 0, [])

    for sol in solutions:
        print(sol)
