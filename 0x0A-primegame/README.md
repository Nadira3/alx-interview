# Prime Game

This project is part of the **ALX Backend Specialization curriculum** and focuses on solving a competitive game scenario using prime numbers, game theory, and algorithm optimization.

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [Usage](#usage)
- [Resources](#resources)
- [License](#license)

## Description
Maria and Ben are playing a game involving consecutive integers starting from 1 up to and including `n`. 
- They take turns choosing a prime number and removing it along with all its multiples from the set. 
- The player unable to make a move loses the game.

The program determines the winner of multiple rounds based on optimal play, assuming Maria always starts.

## Requirements
- **Python version:** 3.4.3 or later
- **OS:** Ubuntu 20.04 LTS
- **Style Guide:** PEP 8 (version 1.7.x)
- **Editor Restrictions:** Only `vi`, `vim`, or `emacs` allowed

### Mandatory Files
1. `0-prime_game.py` - Contains the solution logic.
2. `README.md` - Explains the project.
3. Make sure all files:
   - End with a new line.
   - Are executable.
   - Start with `#!/usr/bin/python3`.

## Tasks

### Task 0: Prime Game
**Mandatory**

Implement the function:
```python
def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): Number of rounds to play.
        nums (list of int): List of `n` values for each round.

    Returns:
        str: "Maria" if Maria wins the most rounds,
             "Ben" if Ben wins the most rounds,
             None if there's a tie.
    """

### Example:
```
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: "Ben"
```

## Usage

1. Clone this repository:
```
git clone https://github.com/<your-username>/alx-interview.git
cd alx-interview/0x0A-primegame
```

2. Run the game:
```
./main_0.py
```

3. Ensure your code passes the example test cases:
```
isWinner = __import__('0-prime_game').isWinner
print(isWinner(5, [2, 5, 1, 4, 3]))  # Expected Output: "Ben"
```


Resources
### Dynamic Programming:
- [Dynamic Programming with Python Examples](https://www.geeksforgeeks.org/dynamic-programming/)

### Python Documentation:
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

## License
This project is copyrighted as part of the **ALX Backend Specialization curriculum**.  
All rights reserved © 2024 ALX.
