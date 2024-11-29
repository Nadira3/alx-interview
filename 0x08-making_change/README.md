# 0x08. Making Change

This project focuses on solving the coin change problem using algorithms, specifically greedy algorithms and dynamic programming, to find the fewest number of coins needed to meet a given total.

## Concepts Covered
- **Greedy Algorithms**: Understand the limitations and application of greedy methods.
- **Dynamic Programming**: Learn how to solve optimization problems using overlapping subproblems and optimal substructure.
- **Algorithmic Complexity**: Analyze and improve time and space complexity.
- **Python Programming**: Efficient implementation of algorithms.

## Requirements
- Python version: 3.4.3
- Code Style: PEP 8 (v1.7.x)
- OS: Ubuntu 20.04 LTS
- A `README.md` file is mandatory at the root of the project directory.

## Prototype
```python
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations.
        total (int): Target amount.

    Returns:
        int: Minimum number of coins required to make up the total.
             Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be met with the available coins.
    """
```

## Example Usage
```
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

### How to Run

1. Clone the repository:
```
git clone https://github.com/<username>/alx-interview.git
```

2. Navigate to the project directory:
```
cd 0x08-making_change
```

3. Execute the main test file:
```
./0-main.py
```


## Learning Resources

**Python Official Documentation**: More Control Flow Tools[https://docs.python.org/3/tutorial/controlflow.html](https://docs.python.org/3/tutorial/controlflow.html)

### GeeksforGeeks Articles:

**Coin Change | DP-7**: [https://www.geeksforgeeks.org/coin-change-dp-7/](https://www.geeksforgeeks.org/coin-change-dp-7/)

**Greedy Algorithm to Find Minimum Number of Coins**: [https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)


## YouTube Tutorials:

**Dynamic Programming - Coin Change Problem**: [(https://www.youtube.com)](https://www.youtube.com)

## License

This project is licensed under the ALX program. All rights reserved © 2024.
