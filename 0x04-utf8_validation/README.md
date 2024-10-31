# 0x04. UTF-8 Validation

## Project Overview

The `0x04-utf8_validation` project aims to implement a function to determine if a given data set represents a valid UTF-8 encoding. This project demonstrates an understanding of the UTF-8 encoding standard, including handling multi-byte characters and correctly interpreting byte patterns according to the UTF-8 format.

### Learning Objectives

- Understand UTF-8 encoding and its format.
- Recognize how multi-byte characters are represented in UTF-8.
- Develop algorithms to validate UTF-8 encoded data.

## Files

### [0-validate_utf8.py](./0-validate_utf8.py)

This file contains the main function `validUTF8(data)` that determines if a given list of integers represents a valid UTF-8 encoding.

## Requirements

- Python 3.x
- Code should be written in accordance with [PEP 8](https://pep8.org/) style guidelines.

## Function Details

### `validUTF8(data)`

- **Parameters**:
  - `data` (list of int): A list of integers where each integer represents a byte (0 <= integer <= 255) in UTF-8 encoded data.
  
- **Returns**:
  - `bool`: `True` if `data` represents a valid UTF-8 encoding, otherwise `False`.

- **Description**:
  - The function inspects each byte in the `data` list to determine if it follows the UTF-8 encoding rules. 
  - The function handles one-byte characters as well as multi-byte characters, ensuring that:
    - The initial byte of multi-byte characters follows UTF-8 starting patterns (e.g., `110xxxxx`, `1110xxxx`, etc.).
    - Subsequent bytes of a multi-byte character follow the `10xxxxxx` pattern.

## Usage

To validate a UTF-8 encoding list, use the following code example:

```python
from 0-validate_utf8 import validUTF8

data = [197, 130, 1]
print(validUTF8(data))  # Output: True

data = [235, 140, 4]
print(validUTF8(data))  # Output: False
```
## Project Structure

README.md: Project documentation.

- 0-validate_utf8.py: Function definition for UTF-8 validation.

tests/: Folder containing unit tests for the validUTF8 function.


## Testing

Unit tests can be found in the tests/ directory. To run the tests, execute the following command:

python3 -m unittest discover tests

Author

Project by Nadira3
