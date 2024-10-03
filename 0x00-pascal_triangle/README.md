# Pascal's Triangle Generator

This project implements a recursive solution to generate Pascal’s Triangle up to a specified number of rows. The solution uses two recursive functions to build the triangle row by row and element by element.

## How It Works

Pascal's Triangle is a triangular array of binomial coefficients. Each number in the triangle is the sum of the two numbers directly above it. The first and last numbers of each row are always `1`.

This implementation leverages two recursive functions:
1. **`recurse_column`**: This function manages adding rows to the triangle.
2. **`recurse_row`**: This function builds each row by computing its elements based on the previous row.

### Example of Pascal's Triangle for `n = 5`:

```plaintext
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```

## Functions

recurse_column(triangle, start, stop)

### Purpose: 

Recursively generates and appends rows to Pascal's Triangle.

### Parameters:

triangle: The current state of the triangle (a list of lists).

start: The current row index being processed.

stop: The total number of rows to generate.


### Returns: 

The complete Pascal's Triangle.


recurse_row(triangle, new_row, start, stop)

### Purpose: 

Recursively generates each row of Pascal’s Triangle by calculating its elements from the previous row.

### Parameters:

triangle: The current state of the triangle (list of lists).

new_row: The row being constructed.

start: The index of the element being processed.

stop: The index of the row to generate.


### Returns:

A completed row for Pascal's Triangle.


pascal_triangle(n)

### Purpose:

Initializes Pascal's Triangle and calls the recursive functions to generate the full triangle.

### Parameters:

n: The number of rows to generate.


### Returns:

Pascal's Triangle with n rows.


## Usage

To use the Pascal's Triangle generator, simply call the pascal_triangle(n) function with n as the number of rows you want to generate.

Example:

# Generate Pascal's Triangle with 5 rows
triangle = pascal_triangle(5)
print(triangle)

## File Structure

├── pascal_triangle.py   # Main file containing the functions
├── README.md            # This README file

Prerequisites

Python 3.x


How to Run

1. Clone the repository.


2. Open the terminal in the project directory.


3. Run the script:



python3 pascal_triangle.py
