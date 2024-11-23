# Rotate 2D Matrix

## Project Overview

This project focuses on implementing an in-place algorithm to rotate a given n x n 2D matrix by 90 degrees clockwise. The task challenges your ability to manipulate matrices and optimize space complexity by performing the operation in-place.

## Task Description

- **Objective**: Given an n x n 2D matrix, rotate it 90 degrees clockwise.
- **Prototype**: `def rotate_2d_matrix(matrix):`
- **Constraints**: 
  - You must modify the matrix in-place, meaning no new matrices should be created.
  - The matrix will always be a square matrix (i.e., `n x n`), and it will not be empty.

## Concepts to Master

- **Matrix Representation in Python**: Understand how to represent a 2D matrix using lists of lists and how to manipulate its elements.
- **In-place Operations**: Modify the matrix without creating a copy to minimize space complexity.
- **Matrix Transposition**: Swap the rows and columns of the matrix.
- **Row Reversal**: Reverse each row after transposition to achieve the 90-degree rotation.
- **Nested Loops**: Use nested loops to iterate through matrix elements.

## Approach

1. **Transpose the Matrix**: Swap the matrix's rows with its columns. This step turns the rows into columns.
2. **Reverse Each Row**: After transposing, reverse each row in place to complete the 90-degree clockwise rotation.

## Code Implementation
see file 

### Example

Given the matrix:
```
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
After calling rotate_2d_matrix(matrix), the matrix will be:
```
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```
### Running the Code

You can test the function using the provided main_0.py file:
```
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```
Run the script:
```
$ ./main_0.py
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```
## Requirements

Allowed Editors: vi, vim, emacs

Python Version: 3.8.10 (Ubuntu 20.04 LTS)

## File Requirements:

All files must be executable.

Code must follow pycodestyle style guide (version 2.8.0).

Every file must end with a new line.

The first line of every file should be #!/usr/bin/python3.

## Resources

Python Official Documentation:

Lists

Data Structures

GeeksforGeeks Articles:

Inplace Rotate Square Matrix by 90 Degrees

Transpose a Matrix in Python

## Conclusion

By understanding matrix manipulation, in-place operations, and transposition, you will be able to implement an efficient 90-degree rotation for square matrices. This project tests your problem-solving skills and your ability to optimize space complexity in Python.




