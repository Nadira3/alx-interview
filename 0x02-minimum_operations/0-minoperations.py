#!/usr/bin/python3

"""
module that contains minimum_operations implementation
"""


def minOperations(n: int):
    """
    Parameters:
                n: int; number of characters to be printed

    Return:
                operations: int
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Factorize the number and count the operations
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
