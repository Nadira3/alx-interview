# N-Queens Solver

This is a Python program that solves the N-Queens problem, placing `N` non-attacking queens on an `N x N` chessboard.

## Usage

```bash
./nqueens N
```

N: an integer ≥ 4, representing the size of the board and the number of queens.


## Requirements

1. If the program is called with the wrong number of arguments, it prints:

Usage: nqueens N

and exits with status 1.


2. If N is not a valid integer, it prints:

N must be a number

and exits with status 1.


3. If N is an integer less than 4, it prints:

N must be at least 4

and exits with status 1.


## Output

Each solution to the N-Queens problem is printed on a new line.

Solutions are represented as lists of [row, column] pairs, where each pair specifies the position of a queen.


Example
```
$ ./nqueens 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

Each line represents a valid solution where no two queens threaten each other.
