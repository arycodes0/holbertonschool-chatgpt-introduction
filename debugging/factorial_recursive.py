#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given number recursively.

    Parameters:
    - n (int): The number for which factorial is to be calculated.

    Returns:
    int: The factorial of the input number 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the argument from the command line and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)
