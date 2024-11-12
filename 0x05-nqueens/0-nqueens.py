#!/usr/bin/python3

""" nqueens implementation """
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def validate_input():
    if len(sys.argv) != 2:
        print_usage_and_exit()
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    return n

def is_safe(board, row, col):
    # Check if there’s a queen in the same column or diagonals
    for i in range(row):
        if (board[i] == col or
            board[i] - i == col - row or
            board[i] + i == col + row):
            return False
    return True

def solve_nqueens(n, row, board, solutions):
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1  # Backtrack

def main():
    n = validate_input()
    solutions = []
    board = [-1] * n
    solve_nqueens(n, 0, board, solutions)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
