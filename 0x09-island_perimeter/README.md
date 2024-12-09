Here’s the README.md file and solution in Python for the "Island Perimeter" task:

README.md

# Island Perimeter

## Description
This project involves calculating the perimeter of an island represented in a 2D grid. Each cell in the grid is either water (`0`) or land (`1`). The goal is to compute the perimeter of the island by considering its edges that touch water or the boundary of the grid.

### Problem Statement
The function `island_perimeter(grid)` takes a 2D list (`grid`) as input and returns the perimeter of the island described in the grid. 

### Constraints
- `0` represents water, and `1` represents land.
- Cells are connected horizontally or vertically (not diagonally).
- The grid is rectangular, with a maximum width and height of 100.
- The island has no lakes (water inside the island).
- The grid is entirely surrounded by water.

### Example
Given the grid:
```plaintext
[
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

The perimeter of the island is 12.

### Usage

Run the program using the 0-main.py script provided:
```
./0-main.py
```

### Requirements

Python 3.x

PEP 8 style guide compliance

No additional modules


### Files

0-island_perimeter.py: Contains the function island_perimeter(grid).

0-main.py: Script to test the function.

README.md: Project description.


### Author

ALX Interview Project

---

## Test Script (0-main.py)
```
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Expected output: 12

```
---

### Explanation

1. **Iterate through the grid**: Loop through each cell in the grid.


2. **Count the perimeter**:

Add 4 for every land cell (1).

Subtract 2 for each land cell adjacent vertically or horizontally (shared edges).



3. **Edge cases**:

Grid boundaries automatically count as water, so no extra checks are needed for the grid edges.

No lakes are present, simplifying the implementation.




### How to Run

1. Clone the repository.


2. Navigate to the directory 0x09-island_perimeter.


3. Make the files executable:
```
chmod +x 0-island_perimeter.py 0-main.py
```

4. Run the main script:
```
./0-main.py
```
