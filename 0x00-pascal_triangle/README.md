# Pascal's Triangle Generator

This project implements a recursive approach to generate Pascal's Triangle up to a specified number of rows.

## Table of Contents
- [Overview](#overview)
- [Functions](#functions)
  - [recurse_column](#recurse_column)
  - [recurse_row](#recurse_row)
  - [pascal_triangle](#pascal_triangle)
- [Usage](#usage)
- [Examples](#examples)
- [How Pascal's Triangle Works](#how-pascals-triangle-works)
- [Future Improvements](#future-improvements)

## Overview
The task involves writing a Python program that generates Pascal's Triangle up to a specified number of levels (`n`). The triangle is built recursively, where each element is the sum of the two elements directly above it in the previous row. The edge elements of each row are always `1`.

## Functions

### `recurse_column(triangle, n)`
This function recursively builds each row of Pascal's Triangle. It adds rows to the triangle one by one until the desired number of rows (`n`) is reached.

- **Parameters:**
  - `triangle`: The list that holds the generated rows of Pascal's Triangle.
  - `n`: The total number of rows to generate.

- **Returns:**
  - The complete Pascal's Triangle (a list of lists).

### `recurse_row(triangle, new_row, n, i)`
This function generates a single row of Pascal's Triangle based on the last row in the triangle. It appends values to `new_row` until the row is complete.

- **Parameters:**
  - `triangle`: The list holding the current rows of Pascal's Triangle.
  - `new_row`: The row currently being built.
  - `n`: The current column index within the row being built.
  - `i`: The index of the row being generated.

- **Returns:**
  - The fully generated row.

### `pascal_triangle(n)`
This function initializes Pascal's Triangle generation by starting with the first row (`[1]`).

- **Parameters:**
  - `n`: The total number of rows to generate.

- **Returns:**
  - The full Pascal's Triangle.

## Usage
1. Clone the repository or download the script.
2. Run the script using Python.
3. Call the `pascal_triangle(n)` function with `n` being the number of rows you want to generate.

```python
n = 5
triangle = pascal_triangle(n)
print(triangle)
```

Example Output

For n = 5, the output will be:
```
[
  [1],
  [1, 1],
  [1, 2, 1],
  [1, 3, 3, 1],
  [1, 4, 6, 4, 1]
]
```
How Pascal's Triangle Works

Pascal's Triangle is a triangular array of binomial coefficients. Each number is the sum of the two numbers directly above it. The first and last elements of each row are always 1.

For example:

Row 0: [1]

Row 1: [1, 1]

Row 2: [1, 2, 1]

Row 3: [1, 3, 3, 1]

Row 4: [1, 4, 6, 4, 1]


Future Improvements

Error handling: Add input validation for non-integer or negative inputs.

Optimization: Refactor the recursion for larger values of n to improve efficiency.

Visualization: Add a visual representation of Pascal's Triangle.

